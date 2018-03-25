import os
import sys

def get_files(rmScriptName=True):
    pathAbs = script_path()
    files = os.listdir()
    if rmScriptName:
        scriptName = sys.argv[0]
        files.remove(scriptName)
    return files

def script_path(fileName=""):
    pathOut = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(pathOut)
    if fileName:
        pathOut = os.path.join(pathOut, fileName)
    return pathOut

def write_file(fileName, content, endline="\n", overWrite=False, subPath="", response=True, rmSign=[]):
    if not content:
        return False
    contentType = type(content)
    if contentType in (list, tuple):
        pass
    elif contentType in (int, str):
        content = [str(content)]
    elif contentType is (dict):
        content = list(content.items())
    else:
        return False
    if overWrite:
        mode="w"
    else:
        mode="a"
    path = script_path()
    if subPath:
        path = os.path.join(path, subPath)
        if not os.path.exists(path):
                os.makedirs(path)
    path = os.path.join(path, fileName)
    with open(path, mode) as file:
        for item in content:
            if rmSign:
                for sign in rmSign:
                    item = (str(item)).replace(sign, "")
            file.writelines(str(item)+endline)
        file.close()
        if response:
            print("--< written to: {0} | contentType: {1}".format(fileName, contentType))
    return True

if __name__=="__main__":
    args = sys.argv[1:]
    files = get_files()
    if "-h" in args:
        print("Usage:")
        print("-p print list of files in current dir")
        print("-w write list of files to .txt in subdir")
        print("-h print this usage info")
    elif "-p" in args:
        for item in files:
            print(item)
    elif "-w" in args:
        write_file(fileName="files.txt",
                   content=files,
                   subPath="DIR_FILES",
                   overWrite=True)
    else:
        print(files)
