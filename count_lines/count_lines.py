import sys
import os
from pathlib import Path


def script_path():
    """set current path, to script path"""
    current_path = str(Path(__file__).parent)
    os.chdir(current_path)
    return current_path
    
    
def read_file(filename):
    """read from file"""
    content = ''
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print('[x] FileNotFoundError: {}'.format(filename))
    return content
    
    
def list_directory_files(directory):
    """https://stackoverflow.com/questions/9816816/get-absolute-paths-of-all-files-in-a-directory"""
    for (dirpath, _, filenames) in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))
            
            
if __name__ == "__main__":
    script_path()
    files = list_directory_files('.')
    python_files = [item for item in files if item.endswith('.py')]
    
    total_lines_count = 0
    total_non_empty_lines_count = 0
    for index, path in enumerate(python_files):
        content = read_file(path)
        lines = content.splitlines()
        lines_number = len(lines)
        non_empty_lines_number = len([line for line in lines if line.strip()])
        
        print('{}) {}, {}'.format(index+1, lines_number, non_empty_lines_number))
        total_lines_count += lines_number
        total_non_empty_lines_count += non_empty_lines_number
    
    print('total_lines_count: {}'.format(total_lines_count))
    print('total_non_empty_lines_count: {}'.format(total_non_empty_lines_count))
    