import io
import os
import subprocess
import sys
import time
from pathlib import Path
from contextlib import redirect_stdout
from pdf_parser import Main  # https://github.com/DidierStevens/DidierStevensSuite/blob/master/pdf-parser.py


def script_path():
    """set current path, to script path"""
    current_path = str(Path(__file__).parent)
    os.chdir(current_path)
    return current_path
    
    
def timer(func):
    """timer decorator for debug"""
    def f(*args, **kwargs):
        before = time.time()
        val = func(*args, **kwargs)
        after = time.time()
        print(f'elapsed: {after-before:.4f}[s] ({func.__name__})')
        return val
    return f
    
    
@timer
def call_inject():
    args = ['.\\pdf_parser.py', '.\\javascript.pdf', '--object', '7']
    sys.argv = args
    stream = io.StringIO()
    with redirect_stdout(stream):
        Main()
    response = stream.getvalue()
    return response
    
    
@timer
def call_subprocess():
    command = ['py', '-3.9', '.\\pdf_parser.py', '.\\javascript.pdf', '--object', '7']
    response = subprocess.getoutput(command)
    return response
    
script_path()

# inject args
response = call_inject()
print(response)

# use subprocess
response = call_subprocess()
print(response)


"""
elapsed: 0.0020[s] (call_inject)
obj 7 0
 Type: /Action
 Referencing:

  <<
    /Type /Action
    /S /JavaScript
    /JS "(app.alert({cMsg: 'Hello from PDF JavaScript', cTitle: 'Testing PDF JavaScript', nIcon: 3});)"
  >>



elapsed: 0.1300[s] (call_subprocess)
obj 7 0
 Type: /Action
 Referencing:

  <<
    /Type /Action
    /S /JavaScript
    /JS "(app.alert({cMsg: 'Hello from PDF JavaScript', cTitle: 'Testing PDF JavaScript', nIcon: 3});)"
  >>
"""
