import os
import sys

def script_path():
    '''change current path to script one'''
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    return path

def start_shell():
    print("\t{}  internal shell started  {}".format(15*"*", 15*"*"))
    while True:
        command = input(">>> ")
        if command == "quit":
            print(">>> exiting from shell...")
            break
        try:
            os.system(command)
        except:
            print(">>> failed to run command...")
    return True
    
if __name__ == "__main__":
    path = script_path()
    start_shell()
