#!/usr/bin/python3
#simple shell window chart generator
import random
from collections import Counter
print("\n" + 20*"<*>" + "\n")

def histogram():
    print("use this for histograms")

def shift_list(l, n):
        return l[n:] + l[:n]

def replace(s, pos, sign):
    return "".join(list(s)[:pos]+[sign]+list(s)[pos+1:])

def get_gauss(elements=20, top=15, sigma=2):
    values = Counter([round(random.gauss(top, sigma)) for x in range(elements)])
    #values = Counter(values)
    values = list(values.items())
    return values

def some_chart(data=[]):
    if not data:
        return False
    else:
        xline = get_xline(data)
    lines = []
    yV = max([x[1] for x in data]) + 5 
    xV = 80
    SQ = chr(0x25a0)
    print(data)
    for x in range(yV):
        yrange = str(yV-x)
        line = " "*(3-len(str(yV-x))) + yrange + "|" + (len(xline)-5)*" "
        for key, value in data:
            xpos = xline.find(str(key))
            ypos = value
            if ypos >= int(yrange):
                #line = line[:xpos] + SQ
                line = replace(line, xpos, SQ)
                #pass 
            #print(xpos, ypos)
        #lines.append(line + SQ*(x))
        lines.append(line)
    lines.append(2*" " + "0|" + len(xline)*"_")
    lines.append(xline)
    for line in lines:
        print(line)

def get_xline(data):
    #make it for both dictio & lists
    xvalues = [x[0] for x in data]
    xvalues.sort()
    xline = 5*" "
    for item in xvalues:
        xline += "  " + str(item)
    if len(xline)<80:
        return xline
    else:
        return ""

def ascii_signs():
    print(chr(4043))


if __name__=="__main__":
    gauss = get_gauss(elements=40, top=10, sigma=1)
    some_chart(data=gauss)


