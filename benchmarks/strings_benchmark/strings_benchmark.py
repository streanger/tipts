import os
import re
import subprocess
import time
from pathlib import Path
from rich import print


def timer(func):
    """timer decorator for debug"""
    def f(*args, **kwargs):
        before = time.time()
        val = func(*args, **kwargs)
        after = time.time()
        print(f"[*] elapsed time: {after - before:.6f}\[s] ([cyan]{func.__name__}[/cyan])")
        return val
    return f


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


@timer
def strings_subprocess(path, n=3):
    """
    get strings from specified file(path) using external strings tool
    strings must be present in system

    :param path: path to file
    :type path: str

    :param n: minimal number of characters
    :type n: int
    """
    command = ['strings', '-nobanner', '-n', str(n), path]
    response = subprocess.getoutput(command)
    out = response.splitlines()
    return out


@timer
def strings(data: bytes=None, path: str=None, n=3):
    """
    get strings from specified data or file(path)

    :param data: data to get strings from
    :type data: bytes

    :param path: path to file
    :type path: str

    :param n: minimal number of characters
    :type n: int

    https://catonmat.net/my-favorite-regex
    """
    if (data is None) and (path is None):
        raise Exception('neither data or path specified')
    elif (data is not None) and (path is not None):
        raise Exception('specify data or path, not both')
    elif (type(data) is bytes) and (path is None):
        pass
    elif (data is None) and (type(path) is str):
        data = Path(path).read_bytes()
    else:
        raise Exception('wrong type of params specified, use help(strings)')
    out = [item for item in re.findall(b'[ -~]+', data) if len(item) >= n]
    return out


@timer
def strings_map(data: bytes=None, path: str=None, n=3):
    """
    get strings from specified data or file(path)

    :param data: data to get strings from
    :type data: bytes

    :param path: path to file
    :type path: str

    :param n: minimal number of characters
    :type n: int

    https://catonmat.net/my-favorite-regex
    """
    if (data is None) and (path is None):
        raise Exception('neither data or path specified')
    elif (data is not None) and (path is not None):
        raise Exception('specify data or path, not both')
    elif (type(data) is bytes) and (path is None):
        pass
    elif (data is None) and (type(path) is str):
        data = Path(path).read_bytes()
    else:
        raise Exception('wrong type of params specified, use help(strings)')
    out = list(filter(lambda x: len(x) >= n, re.findall(b'[ -~]+', data)))
    return out


if __name__ == "__main__":
    os.chdir(str(Path(__file__).parent))
    paths = [
        'c90dd4b5d8534aeca0bd871151e705ba.png',  # ~32KB
        'f98d86f96c541b1fcbaf88f4b2e998d8.png',  # ~1MB
    ]
    min_chars = 6
    for path in paths:
        size = os.path.getsize(path)
        human_size = convert_bytes(size)
        print(f'[*] {path} -> {human_size}')
        out1 = strings_subprocess(path, n=min_chars)
        print(f'[*] {len(out1)=}')
        out2 = strings(path=path, n=min_chars)
        print(f'[*] {len(out2)=}')
        out3 = strings_map(path=path, n=min_chars)
        print(f'[*] {len(out3)=}')
        print()
