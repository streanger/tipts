#!/usr/bin/python3
#set point on line in terminal
import sys
from termcolor import colored
from time import sleep
#from __future__ import print_function

def all_indexes(value, data):
    try:
        indexes = [key for key, item in enumerate(data) if item == value]
    except:
        indexes = [0]
    return indexes

def set_point(point=128, lineRange=256):
    lineSymbol = "~"
    pointSymbol = "|" #"*" #"|"
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

    size = lineRange//150 + 1
    if point >= lineRange:
        lineLen = lineRange
        if lineRange > 256:
            lineLen=256
        LINE = "|" + lineSymbol*(lineLen//size) + "|" + str(round(100*(point/lineRange),2)) + "%"
        if point == lineRange:
            return colored(LINE, "cyan")
        else:
            return colored(LINE, "cyan") + " <point out of range>"
    elif point == lineRange:
        LINE = lineSymbol
    elif point == 0:
        lineLen = lineRange
        if lineRange > 256:
            lineLen=256
        LINE = "|" + lineSymbol*(lineLen//size) + "|" + str(round(100*(point/lineRange),2)) + "%"
        return LINE
    else:
        LINE = ""
    for x in range(1, lineRange):
        if x == int(point):
            if x%size == 0:
                #we need to choose
                #LINE += "|" #true position, false lenght of line
                LINE += lineSymbol + pointSymbol   #true lenght of line, false position; put symbol to left or right side
            else:
                LINE += pointSymbol
        else:
            if x%size == 0:
                LINE += lineSymbol
    LINE = "|" + LINE + "|" + str(round(100*(point/lineRange),2)) + "%"
    keys = all_indexes("|", LINE)  #modify from here down
    LINE = LINE[:keys[1]].replace("~~", "<>") + LINE[keys[1]:]
    LINE = colored(LINE[:keys[1]], "cyan") + LINE[keys[1]:]
    return LINE
    #turn this function to return only line which is than modified
    #or just clear expressions from the very top

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) > 1:
        point = int(args[0])
        lineRange = int(args[1])
        LINE = set_point(point, lineRange)
        print(LINE)
        sys.exit()
    else:
        print("final countdown:")
        for x in range(0, 101):
            LINE = set_point(x, 100)
            print("{}".format(LINE), end='\r', flush=True)
            sleep(0.10)
        print()
