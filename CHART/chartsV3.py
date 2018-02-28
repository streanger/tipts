#!/usr/bin/python3
import matplotlib.pyplot as plt
import random
import math
import os
import time
import datetime

from sys import argv, exit
from collections import Counter
from statistics import mean

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
        #in case of data separated by coma, with no \n
        #if "," in fileContent[0]:
        #    fileContent = (fileContent[0].split(','))[:-1]  #and remove the last one
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
    if markerMax:
        for item in markerMax:
            plt.plot(item[0], item[1], 'go', markersize=8)
            plt.plot(item[0], item[1], 'w+', markersize=6)

    start = markerMin[0][0]
    stop = markerMax[0][0]
    plt.annotate('(%s, %s[N])' % (start, data2[start]),
                 xy=(start, data2[start]+0.1),
                 xytext=(start-50, data2[start]+1),
                 arrowprops=dict(facecolor='black', shrink=0.01, width=0.5, headwidth=8)) 
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
    GLOBAL_MAX = max(data)
    GLOBAL_MIN = min(data)
    LOCAL_MAX = []
    LOCAL_MIN = []
    LOCAL = []
    LOCAL_RANGE = 100    #parameter
    for key, value in enumerate(data[1:-LOCAL_RANGE+2]):
        for x in range(LOCAL_RANGE):
            LOCAL.append(data[key+x])
        LOCAL_MAX.append([max(LOCAL), data.index(max(LOCAL))])
        LOCAL_MIN.append([min(LOCAL), data.index(min(LOCAL))])
        LOCAL = []
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
        for x in range(-5, 6):  #parameter
            try:
                SIDE = data[key+x]
                SIDES.append(SIDE)
            except:
                pass
        if LOOK_FOR.lower() == "min":
            if min(SIDES) == value:
                TRUE_EXT.append((key, value))
        elif LOOK_FOR.lower() == "max":
            if max(SIDES) == value:
                TRUE_EXT.append((key, value))
        else:
            return []
        SIDES = []

    EXT_INSIDE = []
    EXT_INSIDE = [item[1] for item in TRUE_EXT if not item[1] in EXT_INSIDE]

    EXT_SIDES = []
    for item in EXT_INSIDE:
        SIDE = [thing for thing in TRUE_EXT if item == thing[1]]
        EXT_SIDES.append(SIDE)
        SIDE = []

    TRUE_EXT = []
    for item in EXT_SIDES:
        LOCAL = []
        for thing in item:
            LOCAL.append(thing)
            if len(LOCAL) > 1:
                if LOCAL[-1][0] - LOCAL[-2][0] == 1:
                    pass #continue anyway
                else:
                    TO_APPEND = (LOCAL[:-1])[round(len(LOCAL[:-1])//2)]
                    TRUE_EXT.append(TO_APPEND)
                    LOCAL = [thing]
        if LOCAL:
            TO_APPEND = (LOCAL)[round(len(LOCAL)//2)]
            TRUE_EXT.append(TO_APPEND)  #append the last item
    return TRUE_EXT

def average(data):
    sumOf = 0
    for item in data:
        sumOf += float(item)
    return sumOf/len(data)

def remove_horizontal(data, diff = 0.1, decPoint=3):
    #manipulate here to shrink chart
    LOCAL = []
    for key, item in enumerate(data):
        LOCAL.append(item)
        if key%50 == 0:    #parameter
            #print("difference:", abs(float(item) - average(LOCAL)))
            if abs(float(item) - average(LOCAL)) > diff[0]:
                startKey = key
                break
    LOCAL = []
    for key, item in enumerate(data[::-1]):
        LOCAL.append(item)
        if key%50 == 0:    #parameter
            #print("difference:", abs(float(item) - average(LOCAL)))
            if abs(float(item) - average(LOCAL)) > diff[1]:
                stopKey = len(data) - key
                break
    OFFSET = -float(data[startKey])
    dataCut = [round(float(x) + OFFSET, decPoint) for x in data[startKey:stopKey]]  #data with offset
    #dataCut = data[startKey:stopKey]
    return dataCut, startKey

def ext_filter(LMIN, LMAX, data, elements):
    topMIN = [x[0] for x in (Counter([item[0] for item in LMIN])).most_common(100)]  #parameter
    topMAX = [x[0] for x in (Counter([item[0] for item in LMAX])).most_common(100)]

    TRUE_MIN = verify_ext(topMIN, data, "min")[:elements]
    TRUE_MAX = verify_ext(topMAX, data, "max")[:elements]

    #TRUE_MIN = TRUE_MIN[:elements]
    #TRUE_MAX = TRUE_MAX[:elements]

    TRUE_MIN.sort(key=lambda tup: tup[0])   #sort by 1st element of tuple
    TRUE_MAX.sort(key=lambda tup: tup[0])

    return TRUE_MIN, TRUE_MAX

def main(commands):
    startUnix = time.time()
    try:
        filename = commands[0]
    except:
        filename = ""
    if not filename:
        data = [round(10*(math.sin(math.pi*x/100)), 2)+12 for x in range(5000)]
    else:
        data = read_file(filename, rmnl=True)
        if not data:
            print("non-file or empty one...")
            exit()
        originalData = data
        data, zeroPoint= remove_horizontal(data, diff=(0.08, 0.1), decPoint=4)   #responses for start|stop data
    data1 = [key for key, value in enumerate(data)]

    LMIN, LMAX = find_extreme(data)
    TRUE_MIN, TRUE_MAX = [], []
    TRUE_MIN, TRUE_MAX = ext_filter(LMIN, LMAX, data, elements=4)  #rmNegative=True
    TRUE_MIN.insert(0, (0, data[0]))    #add start of the chart

    print("POSITIONS:",zeroPoint,zeroPoint+TRUE_MAX[0][0])
    print("Execution time: %s [s]" % (time.time() - startUnix))
    draw_chart(data1, data, TRUE_MIN, TRUE_MAX)


if __name__ == "__main__":
    commands = argv[1:]
    main(commands)


'''
todo:
-int instead of floats
-change parameters vs script execution time
-
-
'''
