import sys
import os
from pathlib import Path


def script_path():
    '''set current path, to script path'''
    current_path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(current_path)
    return current_path
    
    
def directory_files(directory):
    """https://programmingwithswift.com/python-list-all-files-in-directory-and-subdirectories/"""
    full_paths = []
    for path, current_directory, files in os.walk(directory):
        for filename in files:
            full_paths.append(os.path.join(path, filename))
    return full_paths
    
    
if __name__ == "__main__":
    script_path()
    files = directory_files('directory_name')
    files = [item for item in files if item.endswith('.py')]
    all_lines_count = sum([len(Path(filename).read_text().splitlines()) for filename in files])
    lines_without_empty_and_single_comment_count = sum([len([line for line in Path(filename).read_text().splitlines() if line.strip() and not line.strip().startswith('#')]) for filename in files])
    print('all_lines_count: {}'.format(all_lines_count))
    print('lines_without_empty_and_single_comment_count: {}'.format(lines_without_empty_and_single_comment_count))
    
    