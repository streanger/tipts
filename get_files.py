import os

def get_files(rmScriptName=True):
    try:
	    os.chdir(os.path.dirname(__file__))
    except:
	    os.path.dirname(os.path.abspath(__file__))
    pathAbs = os.getcwd()
    files = os.listdir()
    if rmScriptName:
        scriptName = os.path.basename(__file__)
        files.remove(scriptName)
    return files

def get_dir(fileName=""):
    #return our current path
    #if fileName -> return full path
    try:
	    os.chdir(os.path.dirname(__file__))
    except:
	    os.path.dirname(os.path.abspath(__file__))
    pathAbs = os.getcwd()
    if fileName:
        fullPath = pathAbs + "\\" + fileName
        return fullPath
    #path = os.path.join(pathAbs, fileName)
    return pathAbs     
    
def write_file(fileName, content, addNewline=True, overWrite=True, subPath="", response=True):
    if overWrite:
        #create new file each time
        mode = "w"
    else:
        #append to the file
        mode = "a"
    #content should be a list
    result = 0
    #is it empty or not
    if not content:
        result = 1
        return result
    #will create subPath
    newpath = os.path.join(get_dir(), subPath)
    path = os.path.join(newpath, fileName)
    #print("path:", path)
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    with open(path, mode) as file:
        if addNewline:
            for item in content:
                #print("item:", item)
                file.writelines(str(item)+"\n")
        else:
            for item in content:
                file.writelines(str(item))
        file.close()
        if response:
            print("--< written to: %s" % fileName)
    return result
    
    
if __name__=="__main__":
    files = get_files()
    print(files)
    write_file("files_list.txt", files, subPath="listaLista")
    input()