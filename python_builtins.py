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
        'all',
        'any',
        'ascii',
        'bin',
        'bool',
        'breakpoint',
        'bytearray',
        'bytes',
        'callable',
        'chr',
        'classmethod',
        'compile',
        'complex',
        'delattr',
        'dict',
        'dir',
        'divmod',
        'enumerate',
        'eval',
        'exec',
        'filter',
        'float',
        'format',
        'frozenset',
        'getattr',
        'globals',
        'hasattr',
        'hash',
        'help',
        'hex',
        'id',
        'input',
        'int',
        'isinstance',
        'issubclass',
        'iter',
        'len',
        'list',
        'locals',
        'map',
        'max',
        'memoryview',
        'min',
        'next',
        'object',
        'oct',
        'open',
        'ord',
        'pow',
        'print',
        'property',
        'range',
        'repr',
        'reversed',
        'round',
        'set',
        'setattr',
        'slice',
        'sorted',
        'staticmethod',
        'str',
        'sum',
        'super',
        'tuple',
        'type',
        'vars',
        'zip',
        '__import__'
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
