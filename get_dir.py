from os import path, chdir
from sys import argv

def script_path(fileName=""):
    pathOut = path.realpath(path.dirname(argv[0]))
    chdir(pathOut)
    if fileName:
        pathOut = path.join(pathOut, fileName)
    return pathOut

'''
import sys
import os

def script_path(fileName=""):
    pathOut = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(pathOut)
    if fileName:
        pathOut = os.path.join(pathOut, fileName)
    return pathOut
'''
