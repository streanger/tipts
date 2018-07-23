#!/usr/bin/python3
#import numpy as np
#import cv2
import os
import sys
from shutil import copyfile

def script_path(subpath=""):
    if subpath:
        path = os.path.realpath(os.path.dirname(subpath))
    else:
        path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    return path

def save_file(file, image):
    imgDir = "analysed"
    if not os.path.exists(imgDir):
        os.makedirs(imgDir)
    path = os.path.join(imgDir, file)
    cv2.imwrite(path, image)

def list_files():
    path = script_path()
    #fileTypes = (".png", ".jpeg", ".jpg")
    #files = [item for item in os.listdir(path) if item.lower().endswith(fileTypes)]
    files = [item for item in os.listdir(path) if os.path.isfile(item)]
    return files

if __name__ == "__main__":
    args = sys.argv[1:]
    charNumber = 4
    if args:
        if type(args[0]) is int:
            charNumber = args[0]
    script_path()
    newDir = "noDupli"
    if not os.path.exists(newDir):
        os.makedirs(newDir)
    files = list_files()
    noDuplicates = {}
    for file in files:
        noDuplicates[file[:charNumber]] = file
    for key, sn in noDuplicates.items():
        path = os.path.join(newDir, sn)
        copyfile(sn, path)

