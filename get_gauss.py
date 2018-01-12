#!/usr/bin/python3

import random
import matplotlib.pyplot as plt
from collections import Counter
import os
import sys
from termcolor import colored

def get_gauss(elements=50, top=10, sigma=1, roundValue=2):
    values = []
    for x in range(elements):
        values.append(round(random.gauss(top, sigma), roundValue))
    values = Counter(values)
    values = list(values.items())
    sortedValues = sorted(values, key=lambda x: (x[1]))
    return values

def draw_chart(data, data2):
    plt.plot(data, data2)
    plt.ylabel("N pomiarów")
    plt.xlabel("Rozkład wartości")
    plt.grid()
    plt.show()
    #save image in some way

def read_parameters():
    print("put parameters into file")

def get_dir(fileName=""):
    #return our current path; if fileName -> return full path
    try:
        os.chdir(os.path.dirname(__file__))
    except:
        os.path.dirname(os.path.abspath(__file__))
    pathAbs = os.getcwd()
    if fileName:
        fullPath = pathAbs + "\\" + fileName
        return fullPath
    return pathAbs

def write_file(fileName, content, addNewline="\n", response=True, removeSign=[]):
    result = 0
    if not content:
        result = 1
        return result
    path = os.path.join(get_dir(), fileName)
    with open(path, "w") as file:
        if addNewline == True:
            addNewline = "\n"
        else:
            addNewline = ""
        for item in content:
            if removeSign:
                for sign in removeSign:
                    item = (str(item)).replace(sign, "")
                file.writelines(item+addNewline)
            else:
                file.writelines(item+addNewline)
        file.close()
        if response:
            print("--< written to: %s" % colored(fileName, "cyan"))
        #    for item in ["grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]:
        #        print("--< written to: %s" % colored(fileName + " | " + item, item))
    return result

def main(arguments):
    #print(arguments)
    values = get_gauss(elements=1000, top=100, sigma=2, roundValue=0)
    args, value = zip(*values)
    #draw_chart(args, value)
    write_file("gauss_data.txt", values, addNewline=True, response=True, removeSign=["(",")"])


if __name__=="__main__":
    main(sys.argv[1:])
