#!/usr/bin/python3
import matplotlib.pyplot as plt
import random
import math

from numpy import diff
from collections import Counter

def draw_chart(data1, data2):
    plt.plot(data1, data2)
    plt.ylabel("N pomiarów")
    plt.xlabel("Rozkład wartości")
    plt.grid()
    #print(dir(plt))
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
    LOCAL_RANGE = 20
    for key, value in enumerate(data[1:-LOCAL_RANGE+2]):
        for x in range(LOCAL_RANGE):
            LOCAL.append(data[key+x])
        LOCAL_MAX.append([max(LOCAL), data.index(max(LOCAL))])
        LOCAL_MIN.append([min(LOCAL), data.index(min(LOCAL))])
        LOCAL = []
    return LOCAL_MIN, LOCAL_MAX

def ext_filter(LMIN, LMAX):
    cMIN = Counter([item[0] for item in LMIN])
    cMAX = Counter([item[0] for item in LMAX])
    #figure out if min/max value is true extremum

    return 42

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

#dy = calc_diff(data2)
#dy2 = calc_diff(dy)
#draw_chart(data1, data2)
#draw_chart(data1[2:], dy2)

if __name__ == "__main__":
    data1 = [x for x in range(100)]
    data = create_data()
    draw_chart(data1, data)

    LMIN, LMAX = find_extreme(data)
    ext_filter(LMIN, LMAX)


