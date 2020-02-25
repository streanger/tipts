import sys
import os


def script_path():
    current_path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(current_path)
    return current_path
    
    
def simple_read(file):
    data = []
    with open(file, 'r') as f:
        data = f.read().splitlines()
        f.close()
    return data
    
    
def builtins_list():
    '''
    info:
        https://docs.python.org/3/library/functions.html
        
    list from raw txt:
        data = simple_read('builtins.txt')
        builtins = [item.strip()[:-2] for item in data if item.strip()]
        builtins_str = '\n'.join(["'{}',".format(item) for item in builtins])
        print(builtins_str)
    '''
    builtins = [
        'abs',
        'delattr',
        'hash',
        'memoryview',
        'set',
        'all',
        'dict',
        'help',
        'min',
        'setattr',
        'any',
        'dir',
        'hex',
        'next',
        'slice',
        'ascii',
        'divmod',
        'id',
        'object',
        'sorted',
        'bin',
        'enumerate',
        'input',
        'oct',
        'staticmethod',
        'bool',
        'eval',
        'int',
        'open',
        'str',
        'breakpoint',
        'exec',
        'isinstance',
        'ord',
        'sum',
        'bytearray',
        'filter',
        'issubclass',
        'pow',
        'super',
        'bytes',
        'float',
        'iter',
        'print',
        'tuple',
        'callable',
        'format',
        'len',
        'property',
        'type',
        'chr',
        'frozenset',
        'list',
        'range',
        'vars',
        'classmethod',
        'getattr',
        'locals',
        'repr',
        'zip',
        'compile',
        'globals',
        'map',
        'reversed',
        '__import__',
        'complex',
        'hasattr',
        'max',
        'round',
        ]
    return builtins
    
    
def iter_builtins_help():
    builtins = builtins_list()
    print('Python Built-in Functions:\n')
    for key, item in enumerate(builtins):
        print('{}) {}'.format(key+1, item))
        help(item)
        input()
    return True
    
    
def iter_builtins_examples():
    '''todo: make some examples'''
    return True
    
    
if __name__ == "__main__":
    script_path()
    # print(builtins_list())
    iter_builtins_help()
    iter_builtins_examples()
