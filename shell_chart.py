#!/usr/bin/python3
#simple shell window chart generator by some stranger
import random
from collections import Counter


def shift_list(l, n):
    return l[n:] + l[:n]

def replace(s, pos, sign):
    l = list(s)
    l = l[:pos] + [sign] + l[pos+1:]
    replaced = "".join(l)
    return replaced
    #return "".join(list(s)[:pos]+[sign]+list(s)[pos+1:]) #may cause memory error :) 

def get_gauss(elements=20, top=15, sigma=2):
    values = Counter([round(random.gauss(top, sigma)) for x in range(elements)])
    values = list(values.items())
    return values

def some_hist(data=[]):
    if not data:
        return False
    if type(data) is dict:
        data = list(data.items())
    xline = get_xline(data)
    lines = []
    yV = (round(max([x[1] for x in data])//5)+1)*5
    SQ = chr(0x25a0)
    for x in range(yV):
        yrange = yV-x
        line = " "*(3-len(str(yV-x))) + str(yrange) + "|" + (len(xline)-5)*" "
        for key, value in data:
            xpos = xline.find(str(key))
            ypos = value
            if ypos >= yrange:  #try with reverse condition
                line = replace(line, xpos, SQ)
        lines.append(line)
    lines.append(2*" " + "0|" + len(xline)*"_")
    lines.append(xline)
    for line in lines:
        print(line)

def get_xline(data):
    xvalues = [int(x[0]) for x in data]
    xvalues.sort()
    xline = 5*" "
    for item in xvalues:
        xline += "  " + str(item)
    if len(xline)<80:
        return xline
    else:
        return ""


if __name__=="__main__":
    gauss = get_gauss(elements=100, top=10, sigma=2)
    some_hist(data=gauss)  #can put list of list(tuples) or dictio

