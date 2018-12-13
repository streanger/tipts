''' simple wrapper for google tesseract '''

import sys
import os
from PIL import Image
import subprocess

def script_path():
    '''change current path to script one'''
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    return path
    
def simple_read(file_name):
    '''simple_write data to .txt file, with specified strContent'''
    with open(file_name, "r") as file:
        data = file.read()
    return data
    
def text_from_image():
    filename = "test.png"
    outfile = "some"
    lang = "eng"
    tesseractPath = 'D:\\Programy\\Tesseract-OCR\\tesseract.exe'
    
    commands = [tesseractPath, filename, outfile, '-l', lang, 'txt']
    response = subprocess.getoutput(commands)
    text = simple_read(outfile + ".txt")
    return text
    
def read_image_from_pdf(file):
    return True
    
def main():
    return True
    
if __name__ == '__main__':
    path = script_path()
    text = text_from_image()
    print(text)
    
    