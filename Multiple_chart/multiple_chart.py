#multiple charts
import os
import sys
import csv
import random
import time
import math
import matplotlib.pyplot as plt
from matplotlib import get_backend
import pylab

def script_path(fileName=''):
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)  #it seems to be quite important
    if fileName:
        fullPath = os.path.join(path, fileName)
        return fullPath
    return path

def simple_write(file, strContent):
    with open(file, "w") as f:
        f.write(strContent + "\n")
        f.close()
    return True

def list_files(path, filter=''):
    files = [item for item in os.listdir(path) if item.endswith(".csv")]
    if filter:
        files = [item for item in files if item.startswith(filter)]
    return files

def csv_reader(file):
    reader = csv.reader(file)
    content = [item for item in reader]
    return content

def csv_writer(file, dataRows, csvDir="files"):
    #csvDir = "files"
    if not os.path.exists(csvDir):
        os.makedirs(csvDir)
    path = os.path.join(PATH, csvDir)
    path = os.path.join(path, file)
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=" ")
        for row in dataRows:
            writer.writerow(row)
        #print("--< data written to: {}".format(path))
    return True    
    
def draw_plot(data, save):
    #useful site: https://www.python-course.eu/matplotlib_multiple_figures.php
    if not data:
        print("empty data")
        return False
    #plt.plot(data, color="blue", marker='o', markersize='4', linewidth=1)
    #plt.plot(data, marker='o', markersize='4', linewidth=1)
    plt.figure(figsize=(19.2, 10.8))     #this is what i wanted :)
    plt.ylabel("Force[N]")
    plt.xlabel("measure[n]")
    plt.suptitle('multiple chart')
    plt.ylim((0,250))
    plt.grid()
    for item in data:
        plt.plot(item, linewidth=1)
    
    #plt.plot(data, linewidth=1)
    #fig = plt.figure(figsize=(11.0, 8.0))
    #
    
    if False:
        plt.show()
        plt.close()
    if True:
        backend = get_backend()
        if backend == 'QT':
            # Option 1
            # QT backend
            manager = plt.get_current_fig_manager()
            manager.window.showMaximized()
        elif backend == 'TkAgg':
            # Option 2
            # TkAgg backend
            manager = plt.get_current_fig_manager()
            manager.resize(*manager.window.maxsize())        
        elif backend == 'WX':
            # Option 3
            # WX backend
            manager = plt.get_current_fig_manager()
            manager.frame.Maximize(True)


    #manager = plt.get_current_fig_manager()
    #manager.resize(*manager.window.maxsize())
    if save:
        pylab.savefig('multiple_chart.png', dpi=200)
    return plt    

def read_and_covert(file, subPath, rmnl=True):
    if subPath:
        path = os.path.join(PATH, subPath)
        path = os.path.join(path, file)
    else:
        path = os.path.join(PATH, file)
    try:
        with open(path, "r") as f:
            if rmnl:
                content = f.read().splitlines()
            else:
                content = f.readlines()
        values = [float(item) for item in content[0].split()]
        return values
    except:
        return []
    
def draw_chart(data1, data2, lines, markerMin = [], markerMax = []):
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
    for line in lines:
        plt.plot(line[0], line[1])
    if 1:
        plt.show(data)
        plt.close()
    #save image in some way
    
def timer(func):
    def f(*args, **kwargs):
        before = time.time()
        val = func(*args, **kwargs)
        after = time.time()
        print("elapsed time: {} [s]".format(round(after-before,4)))
        return val
    return f

@timer    
def create_random_files(begin, subPath, n=10):
    files = [begin + str(x).zfill(6) + ".csv" for x in range(n)]
    for file in files:
        data = [[round(math.sin(x)*30*random.random()+30,4) for x in range(300)]]
        #data = [[round(random.random()*155,4) for x in range(300)]]
        csv_writer(file, data, csvDir=subPath)        
    return files

@timer
def plot_charts(files, toShow):
    #will save multiple chart
    
    #put fullData to draw_plot
    fullData = [read_and_covert(file, subPath=FILES_PATH, rmnl=True) for file in files]
    plt = draw_plot(fullData, save=True)
    if toShow:
        plt.show()
    return False
    
    
    #iter one by one
    '''
    toSave = False
    for key, file in enumerate(files):
        content = read_and_covert(file, subPath=FILES_PATH, rmnl=True)
        if key == len(files)-1:
            toSave=True
        plt = draw_plot([content], save=toSave)     #as list with one element
    if toShow:
        plt.show()
    '''
    
    return True
    
def main(args):
    if args:
        print(args)
    global PATH; PATH = script_path()
    global FILES_PATH; FILES_PATH = "files"
    '''-------------setup and args-------------'''
    
    filesNo = 10             #10000 -> 97s, 113s, 86s(fullData),
    create_random_files(begin="180722_", subPath=FILES_PATH, n=filesNo)        #just to create random data
    
    files = list_files(FILES_PATH, filter="180722")
    plot_charts(files, toShow=False)
    print("files number: {}".format(filesNo))

    
    
if __name__ == "__main__":
    main(sys.argv[1:])
    
    
    
'''    
date style:
180722_124357.csv

'''