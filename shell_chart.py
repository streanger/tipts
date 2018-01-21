#!/usr/bin/python3
#simple hist chart by some stranger
import random
import sys
from collections import Counter

def get_gauss(elements=20, top=15, sigma=2):
    values = Counter([round(random.gauss(top, sigma)) for x in range(elements)])
    values = list(values.items())
    return values

def some_hist(data=[]):
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
    gauss = get_gauss(elements=100, top=10, sigma=2)
    #gauss = [5,6,4,5,6,3,4,3,5,6,7,4,5,6,5,4,5,6]
    return gauss

def get_opt(args):
    #print(args)
    #can put list of list(tuples) or dictio
    #or just random data in file
    data = example()
    return data

if __name__=="__main__":
    gauss = get_opt(sys.argv[1:])
    some_hist(data=gauss)

