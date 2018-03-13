import os
import sys

def write_file(fileName, content, endline="\n", overWrite=False, response=True, rmSign=[]):
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
    #try:
    #    os.chdir(os.path.dirname(__file__))
    #except:
    #    os.path.dirname(os.path.abspath(__file__))
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    path = os.path.join(path, fileName)
    #path = os.path.join(os.getcwd(), fileName)
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
#write_file("TEST.txt", [1,2,3,4])  #simple usage
