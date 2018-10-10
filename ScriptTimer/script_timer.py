#script for measure execution time of other scripts(including modules load)
import os
import sys
import subprocess
import time

def script_path():
    '''change current path to script one'''
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)  #it seems to be quite important
    return path
    
def timer(func):
    def f(*args, **kwargs):
        before = time.time()
        val = func(*args, **kwargs)
        after = time.time()
        print("elapsed time: {}s".format(after-before))
        return val
    return f

@timer    
def controll_script(script_payload):
    try:
        out = subprocess.check_output(script_payload)
    except:
        print("failed to run script...")
    return True

    
if __name__ == "__main__":
    PATH = script_path()
    script_payload = ['python', 'test_example.py', '100']
    print(script_payload)
    controll_script(script_payload)