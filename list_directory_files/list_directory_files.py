import os
from pathlib import Path


def os_directory_files(directory):
    """https://stackoverflow.com/questions/9816816/get-absolute-paths-of-all-files-in-a-directory"""
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))
            
            
def pathlib_directory_files(directory):
    """https://stackoverflow.com/questions/9816816/get-absolute-paths-of-all-files-in-a-directory"""
    for filepath in Path(directory).glob('**/*'):
        if filepath.is_dir():
            continue
        yield str(filepath.absolute())
        
        
if __name__ == "__main__":
    os.chdir(str(Path(__file__).parent))
    directory = 'directory'
    files1 = list(os_directory_files(directory))
    files2 = list(pathlib_directory_files(directory))
    print(files1)
    print(files2)
    