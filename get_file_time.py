import sys
import os
import datetime

def script_path():
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    return path
    
def get_time(unix):
    date = str(datetime.datetime.fromtimestamp(unix).strftime("%Y-%m-%d %H:%M:%S"))
    return date
    
    
if __name__ == "__main__":
    path = script_path()
    files = os.listdir()
    for file in files:
        unix = os.path.getmtime(file)
        fileTime = get_time(unix)
        print(file, " >>> ", fileTime)
