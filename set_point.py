#!/usr/bin/python3
#set point on line in terminal
import sys
from termcolor import colored
from time import sleep
#from __future__ import print_function
from threading import Thread
import matplotlib.pyplot as plt

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
        LINE = "|" + (lineSymbol*(lineLen//size)).replace("~~", "<>") + "|" + str(round(100*(point/lineRange),2)) + "%"
        #LINE = LINE.replace("~~", "<>") + LINE[keys[1]:]
        if point == lineRange:
            return colored(LINE, "cyan")
        else:
            return colored(LINE, "cyan") + " <point out of range>"
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

def trace_point(lineRange=100, name="final countdown"):
    print(name)
    for x in range(lineRange+1):
        LINE = set_point(x, lineRange)
        print("{}".format(LINE), end='\r', flush=True)
        sleep(0.05)
    print()
    return True

def draw_chart():
    data = [x**3 for x in range(1000)]
    plt.plot(data)
    plt.ylabel("y values[]")
    plt.xlabel("x values[]")
    plt.show()
    return True


if __name__ == "__main__":
    t1 = Thread(target = trace_point, args=(100, ">>> final_countdown:"))
    t2 = Thread(target = draw_chart, args=())
    t1.start()
    t2.start()
