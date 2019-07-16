''' simple wrapper for google tesseract '''

import sys
import os
import time
from PIL import Image
import subprocess
import codecs


def script_path():
    '''change current path to script one'''
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    return path
    
    
def timer(func):
    def f(*args, **kwargs):
        before = time.time()
        val = func(*args, **kwargs)
        after = time.time()
        print("func: {}, elapsed time: {}[s]\n".format(func.__name__, after-before))
        return val
    return f
    
    
def simple_read(file):
    '''simple_write data to .txt file, with specified strContent'''
    # with open(file_name, "r") as file:
    with codecs.open(file, "r", encoding="utf-8", errors='ignore') as f:
        data = f.read()
    return data
    
    
@timer
def text_from_image(file):
    out = "out"
    lang = "eng"
    tesseractPath = 'D:\\Programy\\Tesseract-OCR\\tesseract.exe'
    commands = [tesseractPath, file, out, '-l', lang, 'txt']
    response = subprocess.getoutput(commands)
    text = simple_read(out + '.txt')
    return text
    
    
def read_image_from_pdf(file):
    return True
    
    
def main():
    return True
    
    
if __name__ == '__main__':
    path = script_path()
    file = "brown_fox.png"
    text = text_from_image(file)
    print(text)
    
    
'''
windows, 9.07.2019 --> https://github.com/UB-Mannheim/tesseract/wiki
'''
