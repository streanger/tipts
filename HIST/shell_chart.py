#!/usr/bin/python3
#simple hist chart by some stranger
import random
import sys
import os
from collections import Counter


def read_file(fileName, rmnl=False):
    try:
        os.chdir(os.path.dirname(__file__))
    except:
        os.path.dirname(os.path.abspath(__file__))
    pathAbs = os.getcwd()
    path = os.path.join(pathAbs, fileName)
    try:
        with open(path, "r") as file:
            if rmnl:
                fileContent = file.read().splitlines()
            else:
                fileContent = file.readlines()
            for item in fileContent:
                if not item.isnumeric():
                    fileContent.remove(item)
    except:
        fileContent = []
    return fileContent

def get_gauss(elements=20, top=15, sigma=2):
    values = Counter([round(random.gauss(top, sigma)) for x in range(elements)])
    values = list(values.items())
    return values

def some_hist(data=[], background=False):
    #make some function to filter input data
    if not data:
        return False
    if type(data) is dict:
        data = list(data.items())
    if type(data[0]) not in (list, tuple):
        print(data)
        data = [int(x) for x in data]
        data = list(Counter(data).items())
    xline = get_xline(data)
    yV = (round(max([x[1] for x in data])//5)+1)*5

    SQ = chr(0x25a0)
    lines = []
    for x in range(yV):
        yrange = yV-x
        line = list(" "*(3-len(str(yV-x))) + str(yrange) + "|" + (len(xline)-4)*" ")
        for key, value in data:
            xpos = xline.find(str(key))
            ypos = value
            if ypos >= yrange:  #try with reverse condition
                line[xpos] = SQ
        if background:
            for x,y in enumerate(line):
                if y == " ":
                    line[x] = chr(721)   #puy any sign you want to
        lines.append("".join(line))
    lines.append(2*" " + "0|" + len(xline)*"_")
    lines.append(xline)
    for line in lines:
        print(line)

def get_xline(data):
    xvalues = [int(x[0]) for x in data] #int against dictio
    xvalues.sort()
    xline = 5*" " + "  ".join([str(x) for x in xvalues])
    return xline

def example():
    gauss = get_gauss(elements=600, top=50, sigma=6)
    #gauss = [5,6,4,5,6,3,4,3,5,6,7,4,5,6,5,4,5,6]
    return gauss

def get_opt(args):
    #fix this one

    #print(args)
    #can put list of list(tuples) or dictio or just random data in file
    data = example()
    if "-b" in args:
        background=True
    else:
        background=False
    #fileName = args[0]
    #data = read_file("data.txt", rmnl=True)
    return data, background

if __name__=="__main__":
    dataIn, back = get_opt(sys.argv[1:])
    some_hist(data=dataIn, background=back)


