import sys
import os

def read_file(fileName, rmnl=False):
    #try:
    #    os.chdir(os.path.dirname(__file__))
    #except:
    #    os.path.dirname(os.path.abspath(__file__))
    #path = os.path.join(os.getcwd(), fileName)
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    path = os.path.join(path, fileName)
    try:
        with open(path, "r") as file:
            if rmnl:
                fileContent = file.read().splitlines()
            else:
                fileContent = file.readlines()
    except:
        fileContent = []
    return fileContent
