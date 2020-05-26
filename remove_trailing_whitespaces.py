'''it removing trailing whitespaces as well as right side spaces'''
import sys
import os
import codecs


def script_path():
    '''change current path to script one'''
    current_path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(current_path)
    return current_path
    
    
def read_file(file):
    '''read data from specified file'''
    content = ''
    with codecs.open(file, "r", encoding="utf-8") as f:
        content = f.read()
    return content
    
    
def write_file(file, data):
    '''write data to .txt file, with specified data'''
    with open(file, "w") as f:
        f.write(data)
        f.close()
    return True
    
    
def remove_whitespaces(content):
    lines = content.splitlines()
    converted_lines = []
    for line in lines:
        if not line.strip():
            line = line.strip()
        line = line.rstrip()
        converted_lines.append(line)
    out = '\n'.join(converted_lines)
    return out
    
    
if __name__ == "__main__":
    script_path()
    file = 'clients_scanner.py'
    over_write = True
    content = read_file(file)
    converted = remove_whitespaces(content)
    out = '_out.'.join(file.split('.'))
    if over_write:
        out = file
    write_file(out, converted)
    