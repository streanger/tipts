import os
import sys

def script_path():
    '''change current path to script one'''
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)  #it seems to be quite important
    return path

def get_lines(file_name, currentPath):
    '''read specified file and remove newlines depend on "rmnl" parameter'''
    path = os.path.join(currentPath, file_name)
    try:
        with open(path, "r") as file:
            file_content = file.readlines()
            return len(file_content)
    except:
        return 0
    
if __name__ == "__main__":
    currentPath = script_path()
    files = [item for item in os.listdir() if item.endswith(".txt")]
    files_len = "\n".join([" : ".join([file, str(get_lines(file, currentPath))]) for file in files])
    print(files_len)