import os
import sys

def script_path():
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)  #it seems to be quite important
    return path

def simple_write(file, str_content):
    '''simple_write data to .txt file, with specified str_content'''
    with open(file, "w", encoding='utf-8') as f:
        f.write(str_content)
        f.close()
        print(">>> data written to:", file)
    return True

def read_file(file_name, rmnl=False):
    '''read specified file and remove newlines depend on "rmnl" parameter; encoding types: Latin-1 and UTF-8'''
    path = os.path.join(script_path(), file_name)
    try:
        with open(path, "r", encoding='utf-8') as file:
            if rmnl:
                file_content = file.read().splitlines()
            else:
                file_content = file.readlines()
    except:
        file_content = []
    return file_content    

def convert(data):
    #put your expression here
    converted = [line for line in data if not "???" in line]
    return converted
    
    
if __name__ == "__main__":
    path = script_path()
    args = sys.argv[1:]
    try:
        file = args[0]
    except:
        print("no file specified...")
        sys.exit()
    file_out = "_c.".join(file.split('.'))
    data = read_file(file, rmnl=True)
    converted = "\n".join(convert(data))
    status = simple_write(file_out, converted)