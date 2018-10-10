#!/usr/bin/python3
import math
import os
import sys
#import time

from sys import argv, exit
from collections import Counter
import matplotlib.pyplot as plt
from pylab import savefig

def script_path():
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)  #it seems to be quite important
    return path

def is_float(value):
    try:
        float(value)
        return True
    except:
        return False

'''
def timer(func):
    def f(*args, **kwargs):
        before = time.time()
        val = func(*args, **kwargs)
        after = time.time()
        print("elapsed time: {}s".format(after-before))
        return val
    return f
'''

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

def draw_chart(data1, data2, lines, markerMin = [], markerMax = [], subtitle="example name"):
    plt.plot(data1, data2)
    plt.ylabel("Force[N]")
    plt.xlabel("measure[n]")
    plt.grid()

    if markerMin:
        for item in markerMin:
            plt.plot(item[0], item[1], 'ro', markersize=8)  #8;12
            plt.plot(item[0], item[1], 'w_', markersize=6)  #6;10
        start = markerMin[0][0]
        plt.annotate('(%s, %s[N])' % (start, data2[start]),
                     xy=(start, data2[start]+0.1),
                     xytext=(start-50, data2[start]+1),
                     arrowprops=dict(facecolor='black', shrink=0.01, width=0.5, headwidth=8)) 

    if markerMax:
        for item in markerMax:
            plt.plot(item[0], item[1], 'go', markersize=8)  #8
            plt.plot(item[0], item[1], 'w+', markersize=6)  #6
        stop = markerMax[0][0]
        plt.annotate('(%s, %s[N])' % (stop, data2[stop]),
                     xy=(stop, data2[stop]+0.1),
                     xytext=(stop-50, data2[stop]+1),
                     arrowprops=dict(facecolor='black', shrink=0.01, width=0.5, headwidth=8))
    for line in lines:
        plt.plot(line[0], line[1])
    plt.suptitle(subtitle)
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')       #full window
    # plt.savefig(subtitle.split('.')[0] + ".png")
    if 1:
        plt.show()
        plt.close()


def find_extreme(data=[]):
    if (not data) or (not type(data) is list):
        return [], []
    LOCAL_MAX = []
    LOCAL_MIN = []
    LOCAL_RANGE = 10    #parameter
    for key, value in enumerate(data[1:-LOCAL_RANGE+2]):        #change[1:
        LOCAL = [data[key+x] for x in range(LOCAL_RANGE)]
        LOCAL_MAX.append([max(LOCAL), data.index(max(LOCAL))])
        LOCAL_MIN.append([min(LOCAL), data.index(min(LOCAL))])
    return LOCAL_MIN, LOCAL_MAX

def find_duplicate(value, data):
    duplicates = [item for item in enumerate(data) if item[1] == value]
    return duplicates

def all_indexes(value, data):
    try:
        indexes = [key for key, item in enumerate(data) if item == value]
    except:
        indexes = [0]   #to not cause error while searching for start
    return indexes

def verify_ext(EXT_LIST, data, LOOK_FOR = "MIN"):
    TRUE_EXT = []
    SIDES = []
    duplicates = []
    for item in EXT_LIST:
        duplicates += find_duplicate(item, data)
    for key, value in duplicates:
        for x in range(-55, 46):    #parameter
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

def remove_horizontal(data, diff = (0.1, 0.1), decPoint=3, extractData=False):
    #shrink chart from both sides
    #rebuild this function; its quite important
    startKey = 0
    stopKey = 0
    LOCAL = []
    lines, line1, line2 = [], [], []
    INTERVAL = 25
    for key, item in enumerate(data):
        LOCAL.append(item)
        if key%INTERVAL == 0:    #parameter
            if abs(float(item) - average(LOCAL)) > diff[0]:
                C = average(data[:key-INTERVAL])    #constant value - horizontal line
                hillX = data[key:key+100]
                hillY = [y for y in range(key, key+100)]
                a, b = linreg(hillY, hillX)     #a,b factories on linear function
                line1 = ([0, key],[C, C])
                line2 = ([key-100, key + 300], [(key-100)*a+b, (key+300)*a+b])
                startKey = round((C-b)/a) #(C-b)/a
                #startKey = key     #previous values
                break
    #commenting this 2 lines doesnt cause any errors
    startCorrect = [round(item, 3) for item in data[startKey:startKey+100]]
    startKey += all_indexes(startCorrect[0], startCorrect)[-1] #the last element of indexes

    LOCAL = []
    for key, item in enumerate(data[::-1]):
        LOCAL.append(item)
        if key%50 == 0:    #parameter
            if abs(float(item) - average(LOCAL)) > diff[1]:
                stopKey = len(data) - key
                break
    # OFFSET = -float(data[startKey])
    if not extractData:
        lines = (line1, line2)
        dataCut = data
        startKey = 0
    else:
        dataCut = [round(float(x), decPoint) for x in data[startKey:stopKey]]  #data with offset
        lines = []
    return dataCut, startKey, lines
    #fix this -> find two linear functions and calc cross index

def filter_extreme(LOCAL, data, minmax="", elements=3):
    TOP_VAL = [x[0] for x in (Counter([item[0] for item in LOCAL])).most_common(20)]  #parameter
    TRUE_VAL = verify_ext(TOP_VAL, data, minmax)[:elements]
    TRUE_VAL.sort(key=lambda tup: tup[0])   #sort by 1st element of tuple
    return TRUE_VAL

def trend_data(data_x, data_y):
    a, b = linreg(data_x, data_y)
    #print(a, b)
    trendData = [data_x[0], data_x[-1]], [data_x[0]*a + b, data_x[-1]*a + b]
    return trendData

def linreg(X, Y):
    #calculate trend line -> 'a' & 'b' factories;  not mine
    if not X:
        X = [x for x in range(len(Y))]
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

#@timer
def main(commands):
    try:
        filename = commands[0]
    except:
        filename = ""
    if not filename:
        zeroPoint = 0
        lines = []
        data = [round(5*(math.sin(math.pi*x/100)), 2)+6 for x in range(1000)]   #example data
    else:
        data = read_file(filename, rmnl=True)
        if not is_float(data[0]):
            data = [round(float(item[item.find("=")+2:]),4) for item in data[13:-1]] #consider cut value here
        else:
            data = [float(item) for item in data]
        if not data:
            print("non-file or empty one...")
            out = "POSITIONS:0 0\tno data or can't find"
            return out
        originalData = data
        data, zeroPoint, lines = remove_horizontal(data, diff=(0.2, 0.2), decPoint=4, extractData=True)  #responses for shrink data(chart)
    data1 = [key for key, value in enumerate(data)]

    LMIN, LMAX = find_extreme(data)
    if not LMIN or not LMAX:
        out = "POSITIONS:0 0\tno data or can't find"
        #print("POSITIONS:0 0\tno data or can't find")
        return out
    TRUE_MIN = filter_extreme(LMIN, data, "min", elements=9)
    TRUE_MAX = filter_extreme(LMAX, data, "max", elements=10)
    TRUE_MIN.insert(0, (0, data[0]))    #add start of the chart

    switchPoint = TRUE_MAX[0][0]
    #remove peaks under 1.5N
    if data[switchPoint] < 1.5:
        TRUE_MAX = TRUE_MAX[1:]
        switchPoint = TRUE_MAX[0][0]

    out = ""    
    if data[switchPoint] == max(data):
        #check if switch value means max value, and then return 0,0
        out = "POSITIONS:{} {}".format(0, 0)
    else:
        out = "POSITIONS:{} {}".format(zeroPoint, zeroPoint+switchPoint)
        
    if "-p" in commands:
        draw_chart(data1, data, lines, TRUE_MIN, TRUE_MAX, filename)
    if "-f" in commands:
        force = data[switchPoint]
        if (float(force) < 3.2) or (float(force)*0.96 > 4.8):
            return out + " force: {}[N] <><> value over limits".format(force)
        else:
            return out + " force: {}[N]".format(force)
    else:
        return out


if __name__ == "__main__":
    #commands = argv[1:]
    #out = main(commands)
    #print(out)

    '''
    #uncomment this one, to iter all files in current dir
    path = script_path()
    files = [item for item in os.listdir(path) if item.endswith(".txt")]
    for key, file in enumerate(files):
        out = main([file, "-f", "-p"])
        print(key, file, out)
    '''
'''
todo:
-int instead of floats
-shrink data both sides in smart way    ++
-change parameters vs script execution time
-make getopt
-analyze all way from data in to "POSITIONS:" and remove useless junk
-make it clear at least

16.05.18
średni czas, bez wykresu: 31/14 ~ 0.45s
'''

