import os

def get_dir(fileName=""):
    try:
        os.chdir(os.path.dirname(__file__))
    except:
        os.path.dirname(os.path.abspath(__file__))
    pathOut = os.getcwd()
    if fileName:
        pathOut = os.path.join(pathOut, fileName)
    return pathOut
