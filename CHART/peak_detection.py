#!/usr/bin/python3
import sys, os
from peakutils.peak import indexes
import numpy as np
import matplotlib.pyplot as plt

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
# '''
def draw_chart(data1, data2, markerMin = [], markerMax = []):
    plt.plot(data1, data2)
    plt.ylabel("Force[N]")
    plt.xlabel("measure[n]")
    plt.grid()

    if markerMin:
        for item in markerMin:
            plt.plot(item, data2[item], 'ro', markersize=8)
            plt.plot(item, data2[item], 'w_', markersize=6)
    if markerMax:
        for item in markerMax:
            plt.plot(item, data2[item], 'go', markersize=8)
            plt.plot(item, data2[item], 'w+', markersize=6)
    plt.show()
# '''
def main(args):
    if "-p" in args:
        drawChart = True
    else:
        drawChart = False
    filename = args[0]
    data = read_file(filename, rmnl=True)
    try:
        float(data[0])
        data = [float(item) for item in data]
    except:
         print("here")
         data = [round(float(item[item.find("=")+2:]),4) for item in data[13:-1]]   #consider cut value here or round(xx, 4)
    peaks = list(indexes(np.array(data), thres=3.0/max(data), min_dist=300))
    print("First peak position: %s, force: %s[N]" % (peaks[0], data[int(peaks[0])]))    #returns first value

    if drawChart:
        data1 = [key for key, val in enumerate(data)]
        draw_chart(data1, data, [], peaks)

if __name__ == "__main__":
    main(sys.argv[1:])
