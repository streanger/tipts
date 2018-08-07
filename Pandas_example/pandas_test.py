#just example of pandas script
import pandas as pd
import sys
import os

def script_path():
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)  #it seems to be quite important
    return path

    
if __name__ == "__main__":
    path = script_path()
    some = pd.read_csv("persons.csv", encoding = "ISO-8859-1")
    values = some.values()      #as an array
    print(some)