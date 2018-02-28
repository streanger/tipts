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
    except:
        fileContent = []
    return fileContent

def draw_chart(data1, data2, markerMin = [], markerMax = []):
    plt.plot(data1, data2)
    plt.ylabel("Force[N]")
    plt.xlabel("measure[n]")
    plt.grid()
    if markerMin:
        for item in markerMin:  #can set markers limit e.g markerMin[:3]
            plt.plot(item[0], item[1], 'ro', markersize=12) #6
            plt.plot(item[0], item[1], 'w_', markersize=8) #6      
    if markerMax:
        for item in markerMax:
            plt.plot(item[0], item[1], 'go', markersize=12)
            plt.plot(item[0], item[1], 'w+', markersize=8)
    #add start and top of the button pressure
    start = markerMin[0][0]
    stop = markerMax[1][0]
    #ax = plt.figure().add_subplot(111)
    plt.annotate('(%s, %s[N])' % (start, data2[start]),
                 xy=(start, data2[start]+0.1),
                 xytext=(start-50, data2[start]+1),
                 arrowprops=dict(facecolor='black', shrink=0.01, width=0.5, headwidth=8)) 
    plt.annotate('(%s, %s[N])' % (stop, data2[stop]),
                 xy=(stop, data2[stop]+0.1),
                 xytext=(stop-50, data2[stop]+1),
                 arrowprops=dict(facecolor='black', shrink=0.01, width=0.5, headwidth=8))
    
    #print("start: %s, stop: %s" % (start, stop))        
    #plt.plot([x for x in range(start, stop)], [8 for x in range(start, stop)])
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
    LOCAL_RANGE = 500    #parameter
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
        #this range causes difference
        for x in range(-5, 6):
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
    for item in TRUE_EXT:
        if not item[1] in EXT_INSIDE:
            EXT_INSIDE.append(item[1])
    #print("EXT_INSIDE:", EXT_INSIDE)

    EXT_SIDES = []
    for item in EXT_INSIDE:
        SIDE = []
        for thing in TRUE_EXT:
            if item == thing[1]:
                SIDE.append(thing)
        EXT_SIDES.append(SIDE)
        SIDE = []
    #print("EXT_SIDES:", EXT_SIDES)

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
    LOCAL = []
    for key, item in enumerate(data):
        LOCAL.append(item)
        if key%10 == 0:    #every 100th thing
            #print("difference:", abs(float(item) - average(LOCAL)))
            if abs(float(item) - average(LOCAL)) > diff:
                startKey = key
                break
    LOCAL = []
    for key, item in enumerate(data[::-1]):
        LOCAL.append(item)
        if key%50 == 0:    #every 100th thing
            #print("difference:", abs(float(item) - average(LOCAL)))
            if abs(float(item) - average(LOCAL)) > diff:
                stopKey = len(data) - key
                break
    OFFSET = -float(data[startKey])
    dataCut = [round(float(x) + OFFSET, decPoint) for x in data[startKey:stopKey]]  #data with offset
    #dataCut = data[startKey:stopKey]
    return dataCut

def ext_filter(LMIN, LMAX, data, limit, rmNegative=False):
    #data - full data which contains LMIN & LMAX values
    cMIN = Counter([item[0] for item in LMIN])
    cMAX = Counter([item[0] for item in LMAX])
 
    topMIN = [x[0] for x in cMIN.most_common(20)]   #parameter
    topMAX = [x[0] for x in cMAX.most_common(20)]
    if rmNegative:
        posMIN = [x for x in topMIN if x > 0]
        posMAX = [x for x in topMAX if x > 0]
        topMIN = posMIN
        topMAX = posMAX
    TRUE_MIN = verify_ext(topMIN, data, "min")
    TRUE_MAX = verify_ext(topMAX, data, "max")

    return TRUE_MIN[:limit], TRUE_MAX[:limit]

def main(commands):
    startUnix = time.time()
    try:
        filename = commands[0]
    except:
        filename = ""
    if not filename:
        data = [round(10*(math.sin(math.pi*x/100)), 2)+15 for x in range(5000)]
    else:
        data = read_file(filename, rmnl=True)
        #data = [100*float(x) for x in data]
        data = remove_horizontal(data, diff=0.08, decPoint=3)   #responses for start|stop data
        #data = [round(float(x), 3) for x in data]   #round data in ??
    data1 = [key for key, value in enumerate(data)]

    LMIN, LMAX = find_extreme(data)
    TRUE_MIN, TRUE_MAX = [], []
    TRUE_MIN, TRUE_MAX = ext_filter(LMIN, LMAX, data, limit=3, rmNegative=False)  #rmNegative=True
    TRUE_MIN.insert(0, (0, data[0]))    #add start of the chart
    print("\nLocals min:", TRUE_MIN)
    print("Locals max:", TRUE_MAX)
    
    stopUnix = time.time()
    print("execution time: %s [s]" % (stopUnix - startUnix))

if __name__ == "__main__":
    
    commands = argv[1:]
    main(commands)

    '''
    try:
        filename = commands[0]
    except:
        filename = ""
    if not filename:
        data = [round(10*(math.sin(math.pi*x/100)), 2)+15 for x in range(5000)]
    else:
        data = read_file(filename, rmnl=True)
        #data = [100*float(x) for x in data]
        data = remove_horizontal(data, diff=0.08, decPoint=3)   #responses for start|stop data
        #data = [round(float(x), 3) for x in data]   #round data in ??
    data1 = [key for key, value in enumerate(data)]

    LMIN, LMAX = find_extreme(data)
    TRUE_MIN, TRUE_MAX = [], []
    TRUE_MIN, TRUE_MAX = ext_filter(LMIN, LMAX, data, limit=3, rmNegative=False)  #rmNegative=True
    TRUE_MIN.insert(0, (0, data[0]))    #add start of the chart
    print("\nLocals min:", TRUE_MIN)
    print("Locals max:", TRUE_MAX)
    '''
 
    #draw_chart(data1, data, TRUE_MIN, TRUE_MAX)

    #ask = input("draw chart? (yes/no)\n")
    #if ask.lower() == "yes":
    #    draw_chart(data1, data, TRUE_MIN, TRUE_MAX)

'''
todo:
-int instead of floats
-
-
-
-
'''
        
