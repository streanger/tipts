#!/usr/bin/python3
import matplotlib.pyplot as plt
import random
import math
import os
import sys

from numpy import diff
from collections import Counter

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
    plt.ylabel("N pomiarów")
    plt.xlabel("Rozkład wartości")
    plt.grid()
    if markerMin:
        for item in markerMin[:3]:
            plt.plot(item[0], item[1], 'ro', markersize=6)
            plt.plot(item[0], item[1], 'w+', markersize=6)        
    if markerMax:
        for item in markerMax[:3]:
            plt.plot(item[0], item[1], 'go', markersize=6)
            plt.plot(item[0], item[1], 'w+', markersize=6)
    plt.show()
    #save image in some way

def calc_diff(data):
    dx = 1
    dy = diff(data)/dx
    return dy

def find_extreme(data=[]):
    if (not data) or (not type(data) is list):
        print("no data or wrong type...")
        return False
    GLOBAL_MAX = max(data)
    GLOBAL_MIN = min(data)
    LOCAL_MAX = []
    LOCAL_MIN = []
    LOCAL = []
    LOCAL_RANGE = 200    #parametr do sterowania 200
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
        #this range casues difference with searching
        #for x in range(-10, 11):
        for x in range(-5, 6):
            SIDE = data[key+x]
            SIDES.append(SIDE)
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
    #print("Extremes:", EXT_INSIDE)

    EXT_SIDES = []
    for item in EXT_INSIDE:
        SIDE = []
        for thing in TRUE_EXT:
            if item == thing[1]:
                SIDE.append(thing)
        EXT_SIDES.append(SIDE)
        SIDE = []
    #print("Ext_sides:", EXT_SIDES)

    TRUE_EXT = []
    for item in EXT_SIDES:
        TRUE_EXT.append(item[round(len(item)/2)]) 
        #for now; its certainly wrong if theres parallel extremes in the chart

    return TRUE_EXT

def ext_filter(LMIN, LMAX, data, rmNegative=False):
    #data - full data which contains LMIN & LMAX values
    cMIN = Counter([item[0] for item in LMIN])  #use item[1] rather than item[0]
    cMAX = Counter([item[0] for item in LMAX])
    topMIN = [x[0] for x in cMIN.most_common(100)]   #ostatnia wartość w nawiasie -> parameter do sterowania; poniżej analogicznie
    topMAX = [x[0] for x in cMAX.most_common(100)]
    if rmNegative:
        posMIN = [x for x in topMIN if x > 0]   #data[x] rather than x
        posMAX = [x for x in topMAX if x > 0]
        topMIN = posMIN
        topMAX = posMAX
    #print("\ntopMIN:", topMIN)
    #print("\ntopMAX:", topMAX)
    TRUE_MIN = verify_ext(topMIN, data, "min")
    TRUE_MAX = verify_ext(topMAX, data, "max")

    return TRUE_MIN, TRUE_MAX

def create_data():
    data1 = [x for x in range(100)]
    data2 = [round(math.sin(math.pi*(x/100))*20*((x/10)**2)+random.randrange(20),2) for x in range(100)]
    #try to find this one
    data2[59] = 550
    data2[60] = 500
    data2[61] = 530
    data2[79] = 720
    data2[80] = 650
    data2[81] = 700
    #it const for now
    data2 = [9.0, 7.01, 12.05, 18.17, 7.4, 14.78, 3.35, 3.14, 8.18, 14.52,
             23.18, 19.2, 19.6, 25.42, 28.69, 25.43, 29.67, 38.42, 43.72, 47.58,
             58.02, 71.06, 68.7, 75.97, 92.86, 92.39, 113.56, 115.37, 125.82, 140.9,
             164.62, 171.96, 180.92, 206.47, 202.6, 221.3, 235.53, 253.28, 273.52, 288.22,
             317.34, 325.85, 343.72, 372.89, 380.34, 400.01, 424.86, 455.84, 463.89, 486.96,
             507.0, 519.94, 549.73, 560.31, 591.6, 600.55, 631.09, 646.15, 666.66, 550,
             500, 530, 729.81, 730.51, 743.23, 757.9, 777.44, 782.77, 788.83, 789.55,
             801.84, 800.63, 807.87, 799.47, 816.37, 803.5, 796.79, 803.18, 784.62, 720,
             650, 700, 739.58, 706.36, 680.85, 671.02, 641.81, 609.2, 576.15, 547.63,
             510.61, 465.07, 434.98, 380.34, 346.14, 287.36, 238.01, 189.09, 131.61, 66.57]
    return data2


if __name__ == "__main__":  
    #data = create_data()
    #data = read_file("esc_force.txt", rmnl=True)
    #data = read_file("esc2_force.txt", rmnl=True)
    data = read_file("esc3_force.txt", rmnl=True)
    data = [round(float(x), 3) for x in data]
    data1 = [x for x in range(len(data))]

    LMIN, LMAX = find_extreme(data)
    TRUE_MIN, TRUE_MAX = ext_filter(LMIN, LMAX, data, rmNegative=True)  #rmNegative=True
    print("Locals min:", TRUE_MIN)
    print("Locals max:", TRUE_MAX)

    ask = input("draw chart? (yes/no)\n")
    if ask.lower() == "yes":
        draw_chart(data1, data, TRUE_MIN, TRUE_MAX)

        
