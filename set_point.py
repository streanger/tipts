#!/usr/bin/python3
import sys
from termcolor import colored
#set point on line in terminal

def all_indexes(value, data):
    try:
        indexes = [key for key, item in enumerate(data) if item == value]
    except:
        indexes = [0]
    return indexes

def set_point(point=128, lineRange=256):
    if type(point) is int:
        if point < 0:
            print("<point under zero value> %d/%d" % (point, lineRange))
            return False
    else:
        print("<wrong point type, expected: %s>" % colored("int", "red"))
        return False
    if type(lineRange) is int:
        if point < 0:
            print("<lineRange under zero value> %d/%d" % (point, lineRange))
            return False
    else:
        print("<wrong lineRange type, expected: %s>" % colored("int", "red"))
        return False
    size = lineRange//168 + 1
    lineSymbol = "~"
    if point >= lineRange:
        lineLen = lineRange
        if lineRange > 256: lineLen=256
        LINE = "|" + lineSymbol*(1+lineLen//size) + "|" + str(round(100*(point/lineRange),2)) + "%"
        if point == lineRange:
            print(colored(LINE, "cyan"))
        else:
            print(colored(LINE, "cyan") + " <point out of range>" )
        return False
    elif point == lineRange:
        LINE = lineSymbol
    elif point == 0:
        lineLen = lineRange
        if lineRange > 256: lineLen=256
        LINE = "|" + lineSymbol*(1+lineLen//size) + "|" + str(round(100*(point/lineRange),2)) + "%"
        print(LINE)
        return True
    else:
        LINE = ""
    for x in range(lineRange):
        if x == int(point):
            if x%size == 0:
                LINE += ".|"
            else:
                LINE += "|"
        else:
            if x%size == 0:
                LINE += lineSymbol
    LINE += "|" + str(round(100*(point/lineRange),2)) + "%"
    pointIndex = LINE.index("|")
    LINE = colored("|" + LINE[:pointIndex], "cyan") + LINE[pointIndex:]
    print(LINE)


    #keys = all_indexes("|", LINE)  #modify from here down
    #print(keys)
    #subLine = " "*len(LINE)
    #subLine[keys[0]] == "|"
    #subLine[keys[2]] == "|"
    #print(subLine)
    return True


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) > 1:
        point = int(args[0])
        lineRange = int(args[1])
        set_point(point, lineRange)
        sys.exit()
    else:
        #set_point(0xed, 256)
        #set_point(0x73, 256)
        #set_point(0x34, 256)
        for x in range(70, 80):
            set_point(x, 100)


#think about retur LINE in each case and than modify it, change things etc
