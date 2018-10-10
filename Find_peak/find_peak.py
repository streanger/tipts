#!/usr/bin/python3
import math
import os
import sys

import time
# import matplotlib.pyplot as plt
# from pylab import savefig

def script_path():
    '''set current path to script path, and return it as string'''
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
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

def read_file(fileName):
    try:
        with open(fileName, "r") as file:
            fileContent = file.read().splitlines()
    except:
        fileContent = []
    return fileContent
    
'''
def draw_chart(data, lines, markerMin = [], markerMax = [], subtitle="example name"):
    plt.plot(data)
    plt.ylabel("Force[N]")
    plt.xlabel("measure[n]")
    plt.grid()

    if markerMin:
        for item in markerMin:
            plt.plot(item[0], item[1], 'ro', markersize=8)  #8;12
            plt.plot(item[0], item[1], 'w_', markersize=6)  #6;10
        start = markerMin[0][0]
        plt.annotate('(%s, %s[N])' % (start, data[start]),
                     xy=(start, data[start]+0.1),
                     xytext=(start-50, data[start]+1),
                     arrowprops=dict(facecolor='black', shrink=0.01, width=0.5, headwidth=8)) 

    if markerMax:
        for item in markerMax:
            plt.plot(item[0], item[1], 'go', markersize=8)  #8
            plt.plot(item[0], item[1], 'w+', markersize=6)  #6
        stop = markerMax[0][0]
        plt.annotate('(%s, %s[N])' % (stop, data[stop]),
                     xy=(stop, data[stop]+0.1),
                     xytext=(stop-50, data[stop]+1),
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
'''

def all_indexes(value, data):
    try:
        indexes = [key for key, item in enumerate(data) if item == value]
    except:
        indexes = [0]   #to not cause error while searching for start
    return indexes

def average(data):
    return (sum(data) / (len(data)))

def data_gen(data):
    for item in data:
        yield item
    
def remove_horizontal(data, diff = (0.1, 0.1), decPoint=3, extractData=False):
    '''shrink chart from both sides'''
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
                break
    #commenting this 2 lines doesnt cause any errors
    startCorrect = [round(item, 3) for item in data[startKey:startKey+100]]
    if startCorrect:
        startKey += all_indexes(startCorrect[0], startCorrect)[-1] #the last element of indexes
    else:
        startKey = 0

    LOCAL = []
    for key, item in enumerate(data[::-1]):
        LOCAL.append(item)
        if key%50 == 0:    #parameter
            if abs(float(item) - average(LOCAL)) > diff[1]:
                stopKey = len(data) - key
                break

    DIRECTION = data[startKey] - C <= 0.02
    
    #find out we're right or left
    if DIRECTION:
        # print("left -> right")
        dataGen = data_gen(data[startKey:])
        for key, val in enumerate(dataGen):
            if val - C > 0.02:
                startKey += key
                break
    else:
        # print("right -> left")
        dataGen = data_gen(data[:startKey][::-1])
        for key, val in enumerate(dataGen):
            if val - C <= 0.02:
                startKey -= key
                break
          
    if not extractData:
        lines = (line1, line2)
        dataCut = data
        return data, startKey, lines
    else:
        dataCut = [round(float(x), decPoint) for x in data[startKey:stopKey]]  #data with offset
        lines = []
        return dataCut, startKey, lines
    
def trend_data(data_x, data_y):
    a, b = linreg(data_x, data_y)
    trendData = [data_x[0], data_x[-1]], [data_x[0]*a + b, data_x[-1]*a + b]
    return trendData

def linreg(X, Y):
    '''calculate trend line -> a & b factories;  not mine'''
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

def find_peak(data, parameters, UP):
    '''ps'''
    rangeVal = parameters[0]
    limit = parameters[1]
    peaks = [] 
    for key, value in enumerate(data[rangeVal:-rangeVal]):
        SIDE = data[key:key+rangeVal*2]
        maxVal = max(SIDE)
        minVal = min(SIDE)
        if UP:
            diff = value - minVal
        else:
            diff = maxVal - minVal
        
        if UP:
            minIndex = SIDE.index(minVal)
            
            if minIndex > rangeVal:
                localMax = max(SIDE[round(rangeVal*0.5):minIndex+1])                        #decide which side
            else:
                localMax = max(SIDE[minIndex:round(rangeVal*1.5)])                          #decide which side
            
            if diff > limit and value == localMax and (not value in (SIDE[0], SIDE[-1])):
                peaks.append((key+rangeVal, value))
        else:
            if diff > limit and value == minVal and (not minVal in (SIDE[0], SIDE[-1])):
                peaks.append((key+rangeVal, value))             
    return peaks
    
# @timer
def main(commands):
    try:
        filename = commands[0]
    except:
        filename = ""
    if not filename:
        out = "POSITIONS:{} {}\t>> file not specified or not found... <<".format(0, 0)
        return out
    else:
        data = read_file(filename)
        if not data:
            out = "POSITIONS:{} {}\t>> no data or can't find... <<".format(0, 0)
            return out
        if not is_float(data[0]):
            data = [round(float(item[item.find("=")+2:]),4) for item in data[13:-1]]                        #consider cut value here
        else:
            data = [float(item) for item in data]
        if not data:
            out = "POSITIONS:{} {}\t>> no data or can't find... <<".format(0, 0)
            return out
        originalData = data.copy()
        data, zeroPoint, lines = remove_horizontal(data, diff=(0.6, 0.2), decPoint=4, extractData=True)     #responses for shrink data(chart)

    peaksUp = find_peak(data, (150, 0.2), True)
    peaksUp.extend(find_peak(data, (50, 0.3), True))
    peaksUp = list(set(peaksUp))                            #remove duplicates
    peaksUp = sorted(peaksUp, key=lambda x: x[0])           #sort up for second element
    
    peaksDown = find_peak(data, (150, 0.2), False)
    peaksDown.extend(find_peak(data, (50, 0.3), False))
    peaksDown = list(set(peaksDown))                        #remove duplicates
    peaksDown = sorted(peaksDown, key=lambda x: x[0])       #sort up for second element
    
    
    TRUE_MIN = []
    TRUE_MAX = []
    if not lines:
        TRUE_MIN.insert(0, (0, data[0]))
    else:
        TRUE_MIN.insert(0, (zeroPoint, data[zeroPoint]))

    
    TRUE_MAX.extend(peaksUp)
    TRUE_MIN.extend(peaksDown)
    if not TRUE_MAX:
        TRUE_MAX.insert(0, (0, data[0]))
    switchPoint = TRUE_MAX[0][0]
    

    # remove peaks under 1.5 [N]
    for key, item in enumerate(TRUE_MAX):
        if item[1] > 1.5:
            TRUE_MAX = TRUE_MAX[key:]
            switchPoint = TRUE_MAX[0][0]
            break
    
    out = ""
    if originalData[switchPoint] == max(data) or switchPoint > data.index(max(data)):
        #check if switch value means max value, and then return 0,0
        out = "POSITIONS:{} {}".format(0, 0)
    else:
        out = "POSITIONS:{} {}".format(zeroPoint, zeroPoint+switchPoint)
    
    # if "-p" in commands:
        # draw_chart(data, lines, TRUE_MIN, TRUE_MAX, filename)
    if "-f" in commands:
        force = data[switchPoint]
        if (float(force) < 3.2) or (float(force) > 4.8):
            # draw_chart(data, lines, TRUE_MIN, TRUE_MAX, filename)
            return out + " force: {}[N] <><> value over limits".format(force)
        else:
            return out + " force: {}[N]".format(force)
    else:
        return out


if __name__ == "__main__":
    commands = sys.argv[1:]
    out = main(commands)
    print(out)

    '''
    #uncomment this one, to iter all files in current dir
    startTime = time.time()
    path = script_path()
    files = [item for item in os.listdir(path) if item.endswith(".txt")]      
    for key, file in enumerate(files):
        # out = main([file, "-f", "-p"])
        # out = main([file, "-p"])
        out = main([file, "-f"])
        # out = main([file])
        print(key, file, out)

    endTime = time.time()
    print("total time:", endTime - startTime)
    '''
    
    
'''
04.10.18
-new idea

10.10.18
-data about peaks in tuples, not in list
'''
