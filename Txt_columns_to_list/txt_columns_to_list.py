'''script for converting txt to rows and columns as list in python'''
import os
import sys

def script_path():
    '''return script path, and set it as your current'''
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)  #it seems to be quite important
    return path

def read_and_convert(file_path):
    '''function reads data from txt file and return it as rows and columns lists'''
    try:
        with open(file_path, "r") as file:
            file_content = file.read().splitlines()
    except FileNotFoundError as err:
        file_content = []
        print(err)
        return [], []
    rows = [line.split() for line in file_content if line]
    elements_no = max([len(line) for line in rows])
    rows = [row + ['']*(elements_no-len(row)) for row in rows]
    if rows:
        columns = [[row[x] if row[x] else "" for row in rows] for x in range(elements_no-1)]
    else:
        columns = []    #empty one
    return rows, columns


if __name__ == "__main__":
    args = sys.argv[1:]
    if args:
        file = args[0]
    else:
        file = 'test.txt'
    path = script_path()
    rows, columns = read_and_convert(file)
    print(rows)
    print(columns)
