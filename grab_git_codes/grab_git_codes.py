import os
import sys
import codecs
from pathlib import Path
from rich import print


def script_path():
    """set current path, to script path"""
    current_path = str(Path(__file__).parent)
    os.chdir(current_path)
    return current_path


def list_directory_files(directory):
    """https://stackoverflow.com/questions/9816816/get-absolute-paths-of-all-files-in-a-directory"""
    for (dirpath, _, filenames) in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))


def read_file(filename):
    """read from file"""
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print('[x] FileNotFoundError: {}'.format(filename))
    return content


def write_file(filename, text, mode='w'):
    """write to file"""
    try:
        with codecs.open(filename, mode, encoding='utf-8') as f:
            f.write(text)
    except Exception as err:
        print('[x] Failed to write to file: {}, err: {}'.format(filename, err))
    return None


def make_delimiter(filename):
    delimiter_center = '# {} {} {}'.format('*'*20, filename, '*'*20)
    delimiter_len = len(delimiter_center)
    delimiter_outer = '# {}'.format('*'*(delimiter_len-2))
    delimiter = '{}\n{}\n{}\n'.format(delimiter_outer, delimiter_center, delimiter_outer)
    return delimiter


# download repo
# search through python files and merge them together
script_path()


# ****** clone repos ******
urls = [
    'https://github.com/streanger/tipts',
    'https://github.com/streanger/for-fun',
]
directories = []
for url in urls:
    command = f'git clone {url}'
    print(f'{command=}')
    os.system(command)
    directory = url.split('/')[-1]
    directories.append(directory)
    
    
for directory in directories:
    # ****** list files ******
    print(f'<{directory}>')
    directory = Path(directory)
    files = [Path(item) for item in list_directory_files(directory) if item.endswith('.py')]
    
    # ****** merge files ******
    total_content = ''
    for index, path in enumerate(files):
        filename = path.name
        print(f'{index+1}) {filename}')
        delimiter = make_delimiter(filename)
        content = read_file(path)
        total_content += f'{delimiter}{content}'
        
    # ****** save output ******
    out = f'{directory}.py'
    write_file(out, total_content)
    print(f'{directory} [.py] content saved to: {out}')
    