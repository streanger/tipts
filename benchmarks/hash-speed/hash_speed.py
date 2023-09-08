import os
import json
import sys
import time
import hashlib
import subprocess
from pathlib import Path
from timeit import default_timer as timer
from rich import print


def timer_decorator(func):
    """timer decorator for debug"""
    def f(*args, **kwargs):
        before = time.time()
        val = func(*args, **kwargs)
        after = time.time()
        print(f'[*] elapsed time: {after - before:.4f}\[s] ({func.__name__})')
        return val
    return f


def func_timer(func, *args, **kwargs):
    """timer which calls functions and returns time of execution"""
    start = timer()
    func(*args, **kwargs)
    end = timer()
    time_ms = (end-start)*1000
    return time_ms


def write_json(filename, data):
    """write to json file"""
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(data, fp, sort_keys=True, indent=4, ensure_ascii=False)
    return True


def sizeof(num, suffix="B"):
    """
    https://stackoverflow.com/questions/1094841/get-human-readable-version-of-file-size
    """
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


def create_big_file(path, exist_ok=True):
    if Path(path).exists() and exist_ok:
        print(f'[*] file [cyan]{path}[/cyan] already exists')
        return
    data = b'A'*1024*1024*1024*1  # 1GB
    Path(path).write_bytes(data)
    print(f'[*] file [cyan]{path}[/cyan] created')


# @timer_decorator
def get_hash_python(path, hash_type=None):
    """get hash of file using pure Python
    path [str] - path to file
    hash_type [str] - type of hash to get
    https://stackoverflow.com/questions/1131220/get-the-md5-hash-of-big-files-in-python
    """
    if hash_type == 'md5':
        hash_ = hashlib.md5()
    elif hash_type == 'sha1':
        hash_ = hashlib.sha1()
    elif hash_type == 'sha256':
        hash_ = hashlib.sha256()
    else:
        raise TypeError(f'wrong type of hash_type passed: {hash_type}')
    block_size = 8192
    with open(path, "rb" ) as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            hash_.update(data)
    return hash_.hexdigest()


# @timer_decorator
def get_hash_subprocess(path, hash_type=None):
    """get hash of file using subprocess
    path [str] - path to file
    hash_type [str] - type of hash to get
    """
    allowed_types = {'md5', 'sha1', 'sha256'}
    if not hash_type in allowed_types:
        raise TypeError(f'wrong type of hash_type passed: {hash_type}')
    command = f'certutil -hashfile {path} {hash_type}'
    # print(f'[*] subprocess command: [cyan]{command}[/cyan]')
    response = subprocess.check_output(command)
    digest = response.decode('utf-8').splitlines()[1]
    return digest


def collect_data():
    # inner function to handle data collection
    def collect_per_hash(hash_type):
        hash_python_time = func_timer(get_hash_python, path, hash_type=hash_type)
        print(f'    [*] elapsed: {hash_python_time:.6f}\[ms], {hash_type}, {get_hash_python.__name__}')
        collected[f'hash-python-{hash_type}']['x'].append(size)
        collected[f'hash-python-{hash_type}']['y'].append(hash_python_time)
        hash_subprocess_time = func_timer(get_hash_subprocess, path, hash_type=hash_type)
        print(f'    [*] elapsed: {hash_subprocess_time:.6f}\[ms], {hash_type}, {get_hash_subprocess.__name__}')
        collected[f'hash-subprocess-{hash_type}']['x'].append(size)
        collected[f'hash-subprocess-{hash_type}']['y'].append(hash_subprocess_time)
        
    sizes = [
        1024,               # 1.0KiB
        10*1024,            # 10.0KiB
        100*1024,           # 100.0KiB
        1024*1024,          # 1.0MiB
        10*1024*1024,       # 10.0MiB
        100*1024*1024,      # 100.0MiB
        200*1024*1024,      # 200.0MiB
        500*1024*1024,      # 500.0MiB
        1024*1024*1024,     # 1.0GiB
        2*1024*1024*1024,   # 2.0GiB
        # 10*1024*1024*1024,  # 10.0GiB
    ]

    # data to collect format
    collected = {
        'hash-python-md5': {
            'color': 'lightgreen',
            'x': [],  # [B]
            'y': [],  # [ms]
        },
        'hash-subprocess-md5': {
            'color': 'lime',
            'x': [],
            'y': [],
        },
        'hash-python-sha1': {
            'color': 'deepskyblue',
            'x': [],
            'y': [],
        },
        'hash-subprocess-sha1': {
            'color': 'cyan',
            'x': [],
            'y': [],
        },
        'hash-python-sha256': {
            'color': 'violet',
            'x': [],
            'y': [],
        },
        'hash-subprocess-sha256': {
            'color': 'magenta',
            'x': [],
            'y': [],
        },
    }

    # files
    files_directory = Path('files')
    files_directory.mkdir(exist_ok=True)
    files = [f'{sizeof(size)}.bin' for  size in sizes]

    # iterate
    for index, (filename, size) in enumerate(zip(files, sizes), start=1):
        path = files_directory.joinpath(filename)
        print(f'{index}) [cyan]{path}[/cyan]')
        if path.exists():
            print(f'    [*] file [cyan]{path}[/cyan] already exists')
        else:
            data = b'A'*size
            path.write_bytes(data)
            print(f'    [*] file [cyan]{path}[/cyan] created')

        # collect for md5, sha1, sha256
        collect_per_hash(hash_type='md5')
        collect_per_hash(hash_type='sha1')
        collect_per_hash(hash_type='sha256')

        # vertical space
        print()        
    return collected


if __name__ == "__main__":
    os.chdir(Path(__file__).parent)

    # collect data for chart
    collected = collect_data()
    out = 'collected.json'
    write_json(out, collected)
    print(f'[*] data saved to: {out}')
    sys.exit()

    # check speed for single file
    path = 'big.bin'
    hash_type = 'sha256'
    create_big_file(path, exist_ok=True)
    hash_ = get_hash_python(path, hash_type=hash_type)
    print(f'[*] hash [cyan]{hash_type}[/cyan] got using Python: {hash_}')
    hash_ = get_hash_subprocess(path, hash_type=hash_type)
    print(f'[*] hash [cyan]{hash_type}[/cyan] got using subprocess: {hash_}')
