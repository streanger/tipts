#!/usr/bin/python3
import os
import sys

def script_path():
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)  #it seems to be quite important
    return path

def read_file(fileName, rmnl=False):
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

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("script will convert all tabs in specified file to 4 spaces")
        print("usage:")
        print("     python3 tabs_to_spaces.py someFile.py > newFile.py")
        sys.exit()
    else:
        path = script_path()
        file = args[0]
        if not os.path.exists(file):
            print("no such file...")
            sys.exit()
        fileContent = read_file(file)
        replaced = "".join(fileContent).replace('\t', 4*' ')
        print(replaced)
