'script read data from many files and remove duplicate lines, then print data out'
import os
import sys

def script_path():
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    return path

def read_file(path, rmnl=True):
    try:
        with open(path, "r", encoding="utf-8") as file:
            if rmnl:
                fileContent = file.read().splitlines()
            else:
                fileContent = file.readlines()
    except MemoryError:
        print(">-- memory error")
        fileContent = []
    except:
        fileContent = []
    return fileContent
    
    
if __name__ == "__main__":
    path = script_path()
    args = sys.argv[1:]
    files = [file for file in args if file.endswith('.txt')]
    content = []
    for file in files:
        content.extend(read_file(file))
    setContent = list(set(content))
    print("\n".join(setContent))

    
    
    