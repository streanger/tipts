import os
import sys

def read_file(path, rmnl=False):
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
    args = sys.argv[1:]
    file = args[0]
    print(args)
    content = read_file(file, rmnl=True)
    print(content)
    input("\nenter to exit...\n")