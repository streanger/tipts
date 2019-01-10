import sys
import os
import time
import datetime
import shutil

def script_path():
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    return path
    
    
def get_time(unix, file_form=False):
    if file_form:
        date = str(datetime.datetime.fromtimestamp(unix).strftime("%Y%m%d_%H%M%S"))
    else:
        date = str(datetime.datetime.fromtimestamp(unix).strftime("%Y-%m-%d %H:%M:%S"))
    return date
    
    
def date_to_unix(date):
    out = time.mktime(date.timetuple())
    return out
    
    
def move_file(file, current_path, new_path):
    currentFilePath = os.path.join(current_path, file)
    newFilePath = os.path.join(new_path, file)
    shutil.move(currentFilePath, newFilePath)
    return True
    
    
def make_dir(new_dir):
    ''' make new dir and return new path '''
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    return new_dir
    
    
def main():
    edge_time = date_to_unix(datetime.datetime(2019, 1, 1, 20, 10, 12))   # put some date here
    dir_name = "older_than_" + get_time(edge_time, file_form=True)
    
    current_path = script_path()
    new_path = os.path.join(current_path, make_dir(dir_name))
    
    files = [file for file in os.listdir()]                         # add some filter here
    
    scriptName = os.path.basename(os.path.normpath(sys.argv[0]))
    files.remove(scriptName)                                        # don't move yourself :)
    
    for file in files:
        unix = os.path.getmtime(file)
        fileTime = get_time(unix)                                   # string format
        
        if unix < edge_time:                                        # check if file is older than edge_time
            try:
                move_file(file, current_path, new_path)
                print("file moved: {}".format(file))
            except:
                print("failed to move file: {}".format(file))
    return True
    
    
if __name__ == "__main__":
    main()
    
    
    
    