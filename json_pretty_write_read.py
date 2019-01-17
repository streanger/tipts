import sys
import os
import collections
import json
import pprint


def script_path():
    '''change current path to script one'''
    current_path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(current_path)
    return current_path
    
    
def read_json_to_dict(file):
    with open(file) as f:
        data = json.load(f)
    return data
    
    
def write_to_json(file, data):
    with open(file, 'w') as fp:
        # ensure_ascii -> False/True -> characters/u'type'
        json.dump(data, fp, sort_keys=True, indent=4, ensure_ascii=False)
    return True
    
    
if __name__ == "__main__":
    script_path()
    
    # example of dict data
    data = dict(zip([str(x) for x in range(10)], ["data_" + str(x*2).zfill(2) for x in range(10)]))
    data['4'] = {'some': 'thing', 'next': 'line'}
    
    # save to json
    data = collections.OrderedDict(data)                                    # ordered if needed
    write_to_json('data.json', data)
    
    # read from json
    data = read_json_to_dict('data.json')
    pprint.pprint(data, depth=2, indent=4, width=60)                        # pretty print
    print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))   # print json format
    