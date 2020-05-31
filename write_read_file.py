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
    with codecs.open(file, "w", encoding="utf-8") as f:
        f.write(data)
        f.close()
    return True
    
    
if __name__ == "__main__":
    script_path()
    file = 'file.txt'
    write_file(file, 'test\ntest')
    content = read_file(file)
    print(content)
    