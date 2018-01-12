#!/usr/bin/python3
import random
import matplotlib.pyplot as plt
from collections import Counter
import os
import sys
from termcolor import colored

def get_gauss(elements=50, top=10, sigma=1, roundValue=2, distName="Gauss distribution"):
    values = []
    for x in range(elements):
        values.append(round(random.gauss(top, sigma), roundValue))
    values = Counter(values)
    values = list(values.items())
    #values = sorted(values, key=lambda x: (x[0]))
    values.insert(0, distName)
    return values

def draw_chart(data1, data2):
    plt.plot(data1, data2)
    plt.ylabel("N pomiarów")
    plt.xlabel("Rozkład wartości")
    plt.grid()
    plt.show()
    #save image in some way

def read_parameters(fileName):
    parameters = []
    return parameters

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

def usage():
    print('''Example of get_gauss usage:
--< python3 get_gauss.py parameters.txt fileOut.txt
--< where parameters lookslike:
--<  <Name>    <elements>   <top>   <sigma>
--< param.txt     200        40        2''')
    print("--< for more go to: %s" % colored("https://github.com/streanger", "cyan"))
    print("\n" + 16*"<*>" + "\n")

def main(argIn):
    fileOut = "gauss_data.txt"
    fileIn = ""
    if argIn:
        try:
            fileIn = argIn[0]
            fileOut = argIn[1]
        except:
            print("--< wrong parameters!")
            usage()
    else:
        usage()
    parameters = read_parameters(fileIn)
    for param in parameters:
        values = get_gauss(elements=500, top=40, sigma=2, roundValue=0)
        write_file(fileOut,
                   values,
                   addNewline=True,
                   response=True,
                   removeSign=["(",")"])
    print("--< finished")
    #args, value = zip(*values[1:]) #starts from 1 'cause 0 is name
    #draw_chart(args, value)


if __name__=="__main__":
    main(sys.argv[1:])



