import sys
import os
import textract
from pathlib import Path


def script_path():
    '''set current path to script_path'''
    current_path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(current_path)
    return current_path
    
    
if __name__ == "__main__":
    script_path()
    filename = 'file.pdf'
    text = textract.process(filename)
    
    
"""
install Poppler:
    go to: https://anaconda.org/conda-forge/poppler/files
    unpack it into chosen location
    add Poppler bin location (...\Library\bin) to System PATH
    https://stackoverflow.com/questions/18381713/how-to-install-poppler-on-windows/53960829#53960829
    remember to close/open your app for running code (e.g. npp or IDE)
    
tags:
    extract text from pdf
    pdf to text
    pdf_extract
    parse pdf
"""
