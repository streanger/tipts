#script for controll other script
import os
import sys
import subprocess
import time

def script_path():
    '''change current path to script one'''
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)  #it seems to be quite important
    return path
    
def controll_script(script_payload):
    print(script_payload)
    while True:
        try:
            # subprocess.check_output(script_payload)
            subprocess.call(script_payload)
            while True:
                sleep(0.00001)
        except:
            print("--< exception occured. Script will restart soon.")
            for x in range(5):
                print("wait {}[s]...".format(5-x-1), end='\r', flush=True)
                time.sleep(1)
    return True

if __name__ == "__main__":
    PATH = script_path()
    
    script_payload = ['python', 'test_example.py', '8']
    #script_payload = ['python', 'accHarvestV1.1.py', '-b', 'wrozbita-maciej', '-d', 'dictionaries/8-more-passwords.txt', '-u', '0']
    controll_script(script_payload)
    
    
    
    
    #script_payload = ['python', 'accHarvestV1.1.py', '-b', 'wrozbita-maciej', '-d', 'dictionaries/8-more-passwords.txt', '-u', '0']
    
    