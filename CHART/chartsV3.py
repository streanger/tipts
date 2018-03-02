#!/usr/bin/python3
import matplotlib.pyplot as plt
import random
import math
import os
import time
import datetime

from sys import argv, exit
from collections import Counter


def unix_time(unix=""):
    if not unix:
        unix = time.time()
    return datetime.datetime.fromtimestamp(unix).strftime("%Y.%m.%d %H:%M:%S")

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
    except:
        fileContent = []
    return fileContent

def draw_chart(data1, data2, markerMin = [], markerMax = []):
    plt.plot(data1, data2)
    plt.ylabel("Force[N]")
    plt.xlabel("measure[n]")
    plt.grid()

    if markerMin:
        for item in markerMin:
            plt.plot(item[0], item[1], 'ro', markersize=8)
            plt.plot(item[0], item[1], 'w_', markersize=6)
        start = markerMin[0][0]
        plt.annotate('(%s, %s[N])' % (start, data2[start]),
                     xy=(start, data2[start]+0.1),
                     xytext=(start-50, data2[start]+1),
                     arrowprops=dict(facecolor='black', shrink=0.01, width=0.5, headwidth=8)) 

    if markerMax:
        for item in markerMax:
            plt.plot(item[0], item[1], 'go', markersize=8)
            plt.plot(item[0], item[1], 'w+', markersize=6)
        stop = markerMax[0][0]
        plt.annotate('(%s, %s[N])' % (stop, data2[stop]),
                     xy=(stop, data2[stop]+0.1),
                     xytext=(stop-50, data2[stop]+1),
                     arrowprops=dict(facecolor='black', shrink=0.01, width=0.5, headwidth=8))
    plt.show()
    #save image in some way

def find_extreme(data=[]):
    if (not data) or (not type(data) is list):
        print("no data or wrong type...")
        exit()
    LOCAL_MAX = []
    LOCAL_MIN = []
    LOCAL_RANGE = 50    #parameter
    for key, value in enumerate(data[1:-LOCAL_RANGE+2]):
        LOCAL = [data[key+x] for x in range(LOCAL_RANGE)]
        LOCAL_MAX.append([max(LOCAL), data.index(max(LOCAL))])
        LOCAL_MIN.append([min(LOCAL), data.index(min(LOCAL))])
    return LOCAL_MIN, LOCAL_MAX

def find_duplicate(value, data):
    duplicates = [item for item in enumerate(data) if item[1] == value]
    return duplicates

def verify_ext(EXT_LIST, data, LOOK_FOR = "MIN"):
    TRUE_EXT = []
    SIDES = []
    duplicates = []
    for item in EXT_LIST:
        duplicates += find_duplicate(item, data)
    for key, value in duplicates:
        for x in range(-10, 11):    #parameter
            try:
                SIDES.append(data[key+x])
            except:
                pass
        if LOOK_FOR.lower() == "min":
            if min(SIDES) == value:
                if not (value in (SIDES[0], SIDES[-1])):    #reject flat side(s)
                    TRUE_EXT.append((key, value))
        elif LOOK_FOR.lower() == "max":
            if max(SIDES) == value:
                if not (value in (SIDES[0], SIDES[-1])):    #reject flat side(s)
                    TRUE_EXT.append((key, value))
        else:
            return []
        SIDES = []

    EXT_INSIDE = list(set([item[1] for item in TRUE_EXT]))  #list(set(DOUBLES)) to remove
    EXT_SIDES = [[thing for thing in TRUE_EXT if item == thing[1]] for item in EXT_INSIDE]

    TRUE_EXT = []
    for item in EXT_SIDES:  #select one of extremes which are close to each other
        LOCAL = []
        for thing in item:
            LOCAL.append(thing)
            if len(LOCAL) > 1:
                if not (LOCAL[-1][0] - LOCAL[-2][0] == 1):
                    TRUE_EXT.append((LOCAL[:-1])[round(len(LOCAL[:-1])//2)])    #append center element
                    LOCAL = [thing]
        if LOCAL:
            TRUE_EXT.append(LOCAL[round(len(LOCAL)//2)])
    return TRUE_EXT

def average(data):
    return (sum(data) / float(len(data)))

def remove_horizontal(data, diff = 0.1, decPoint=3):
    #shrink chart from both sides
    #rebuild this function; its quite important
    LOCAL = []
    for key, item in enumerate(data):
        LOCAL.append(item)
        if key%50 == 0:    #parameter
            if abs(float(item) - average(LOCAL)) > diff[0]:
                startKey = key
                break
    LOCAL = []
    for key, item in enumerate(data[::-1]):
        LOCAL.append(item)
        if key%50 == 0:    #parameter
            if abs(float(item) - average(LOCAL)) > diff[1]:
                stopKey = len(data) - key
                break
    OFFSET = -float(data[startKey])
    dataCut = [round(float(x) + OFFSET, decPoint) for x in data[startKey:stopKey]]  #data with offset
    return dataCut, startKey
    #fix this -> find two linear functions and calc cross index

def filter_extreme(LOCAL, data, minmax="", elements=3):
    TOP_VAL = [x[0] for x in (Counter([item[0] for item in LOCAL])).most_common(500)]  #parameter
    TRUE_VAL = verify_ext(TOP_VAL, data, minmax)[:elements]
    TRUE_VAL.sort(key=lambda tup: tup[0])   #sort by 1st element of tuple
    return TRUE_VAL

def trend_data(data_x, data_y):
    a, b = linreg(data_x, data_y)
    #print(a, b)
    trendData = [data_x[0], data_x[-1]], [data_x[0]*a + b, data_x[-1]*a + b]
    return trendData

def simple_chart(data = []):
    if not data:
        data = [(1,4), (2,5), (5,2), (6,3)]
    data_x, data_y = zip(*data)
    #calc trend line
    #a, b = linreg(data_x, data_y)
    plt.plot(data_x, data_y)
    plt.ylim(0,max(data_y)+5)
    trendData = trend_data(data_x, data_y)
    plt.plot(trendData[0], trendData[1])
    plt.grid()
    plt.show()

def linreg(X, Y):
    #calculate trend line -> 'a' & 'b' factories;  not mine
    N = len(X)
    Sx = Sy = Sxx = Syy = Sxy = 0.0
    for x, y in zip(X, Y):
        Sx = Sx + x
        Sy = Sy + y
        Sxx = Sxx + x*x
        Syy = Syy + y*y
        Sxy = Sxy + x*y
    det = Sxx * N - Sx * Sx
    return (Sxy * N - Sy * Sx)/det, (Sxx * Sy - Sx * Sxy)/det

def main(commands):
    #side = commands[1] #should be -10,11 -> range 10 both sides
    #extRange = commands[2] #50 for now; 20-100 should be ok
    #topExt = commands[3]   #500 for now -> 100-1000
    #elements = commands[4] #5; 3-5 is ok

    startUnix = time.time()
    try:
        filename = commands[0]
    except:
        filename = ""
    if not filename:
        zeroPoint = 0
        data = [round(5*(math.sin(math.pi*x/100)), 2)+6 for x in range(1000)]
    else:
        data = read_file(filename, rmnl=True)
        if "TEST.txt" in filename:
            data = [float(item[item.find("=")+2:]) for item in data[13:-1]] #consider cut value here
        else:
            data = [float(item) for item in data]
        if not data:
            print("non-file or empty one...")
            exit()
        originalData = data
        data, zeroPoint= remove_horizontal(data, diff=(0.08, 0.1), decPoint=4)  #responses for shrink data(chart)
    data1 = [key for key, value in enumerate(data)]

    LMIN, LMAX = find_extreme(data)
    TRUE_MIN = filter_extreme(LMIN, data, "min", elements=4)
    TRUE_MAX = filter_extreme(LMAX, data, "max", elements=5)
    TRUE_MIN.insert(0, (0, data[0]))    #add start of the chart

    print("POSITIONS:%s %s" % (zeroPoint,zeroPoint+TRUE_MAX[0][0]))
    #print("Execution time: %s [s]" % (time.time() - startUnix))
    draw_chart(data1, data, TRUE_MIN, TRUE_MAX)


if __name__ == "__main__":
    commands = argv[1:]
    main(commands)
    #simple_chart()

'''
todo:
-int instead of floats
-shrink data both sides in smart way
-change parameters vs script execution time
-make getopt
-analyze all way from data in to "POSITIONS:" and remove useless junk
-make it clear at least
'''

