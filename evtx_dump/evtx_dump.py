import sys
import os
import time
import ctypes
import json
import Evtx.Evtx as evtx  # python-evtx
import pandas as pd
from termcolor import colored

"""
useful:
    https://chapinb.com/python-forensics-handbook/ch03_event_logs.html
"""

def script_path():
    current_path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(current_path)
    return current_path
    
    
def check_if_admin():
    """check if running script as admin"""
    return ctypes.windll.shell32.IsUserAnAdmin()
    
    
def date_now():
    """returns date string"""
    return time.strftime('%Y%m%d')
    
    
def get_events(input_file, parse_xml=False):
    """
    Opens a Windows Event Log and returns XML information from
    the event record.
    """
    with evtx.Evtx(input_file) as event_log:
        for record in event_log.records():
            if parse_xml:
                yield record.lxml()
            else:
                yield record.xml()
                
                
def filter_events_json(event_data, event_ids, fields=None):
    """
    Provide events where the event id is found within the provided list
    of event ids. If found, it will return a JSON formatted object per event.
    """
    for evt in event_data:
        system_tag = evt.find("System", evt.nsmap)
        event_id = system_tag.find("EventID", evt.nsmap)
        if event_id.text in event_ids:
            event_data = evt.find("EventData", evt.nsmap)
            json_data = {}
            for data in event_data.getchildren():
                if not fields or data.attrib["Name"] in fields:
                    # If we don't have a specified field filter list, print all
                    # Otherwise filter for only those fields within the list
                    json_data[data.attrib["Name"]] = data.text
            yield json_data
            
            
def get_hashes():
    """parse sysmon event 1, to get process name and hashes (md5, sha256)"""
    sysmon_evtx_file = 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-Sysmon%4Operational.evtx'
    process_hash = filter_events_json(
        get_events(sysmon_evtx_file, parse_xml=True),
        event_ids=['1'],
        fields = [
            # "Image",
            'OriginalFileName',
            'Hashes',
            ]
    )
    hashes_pairs = []
    for index, data in enumerate(process_hash):
        pair = (data['OriginalFileName'], data['Hashes'])
        hashes_pairs.append(pair)
    hashes_pairs = list(set(hashes_pairs))
    return hashes_pairs
    
    
def get_ips():
    """parse sysmon event 3, to get unique IP's"""
    sysmon_evtx_file = 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-Sysmon%4Operational.evtx'
    ips_events = filter_events_json(
        get_events(sysmon_evtx_file, parse_xml=True),
        event_ids=['3'],
        fields = [
            'Image',
            'SourceIp',
            'DestinationIp',
            ]
    )
    ips_list = []
    for index, data in enumerate(ips_events):
        image = data['Image']
        source_ip = data['SourceIp']
        destination_ip = data['DestinationIp']
        ips_list.append((image, source_ip, destination_ip))
    ips_list = list(set(ips_list))
    return ips_list
    
    
if __name__ == "__main__":
    os.system('color')
    script_path()
    
    # ********** check admin rights **********
    if not check_if_admin():
        print(colored('[x] no admin rights', 'yellow'))
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()
        
    # ********** get event 3 IP's **********
    ips_list = get_ips()
    df = pd.DataFrame(ips_list)
    csv_file = 'sysmon_3_{}.csv'.format(date_now())
    df.to_csv(csv_file)
    print('[*] data saved to file: {}'.format(colored(csv_file, 'cyan')))
    
    # ********** get event 1 hashes **********
    hashes_pairs = get_hashes()
    df = pd.DataFrame(hashes_pairs)
    csv_file = 'sysmon_1_{}.csv'.format(date_now())
    df.to_csv(csv_file)
    print('[*] data saved to file: {}'.format(colored(csv_file, 'cyan')))
    