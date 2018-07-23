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
    #values = list((Counter(values)).items()) #uncomment this for counter values
    values.insert(0, distName)
    return values

def line_gauss(elements=20, top=15, sigma=2, rValue=0, vertical=False):
    #this is kind of shit but works
    VALUES = []
    if not rValue:
        VALUES = [round(random.gauss(float(top), float(sigma))) for x in range(int(elements))]
    else:
        VALUES = [round(random.gauss(float(top), float(sigma)),rValue) for x in range(int(elements))]
    if vertical:
        VALUES = "\n".join([str(item) for item in VALUES])
    return VALUES

def draw_chart(data1, data2):
    plt.plot(data1, data2)
    plt.ylabel("N pomiarów")
    plt.xlabel("Rozkład wartości")
    plt.grid()
    plt.show()
    #save image in some way

def read_parameters(fileName):
    parameters = []
    parameter = []
    path = os.path.join(get_dir(), fileName)
    with open(path, "r") as file:
        content = file.read().splitlines()
    for index, line in enumerate(content):
        parameters.append(line.split())
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
    print('''--< Usage with fileIn, fileOut:
--< python3 get_gauss.py parameters.txt gauss_data.txt
--< parameters in file:
--<  <Name>     <center>  <elements>  <sigma>
--< Gauss_dist     40        200         2
--<
--< Quick line usage:
--< -q(elements,center,sigma) -> e.g. -q10,5,1 to print data in command line
--< -rV -> e.g -r2 round value
--< -v -> print data vertical, if none print as list''')
    print("--< for more go to: %s" % colored("https://github.com/streanger", "cyan"))
    print(16*"<*>" + "\n")

def main(argIn):
    fileOut = "gauss_data.txt"
    fileIn = "parameters.txt"
    if argIn:
        elements = rValue = 0
        vertical = False
        for item in  argIn:
            if "-q" in item:
                try:
                    elements, top, sigma = item[2:].split(",")
                except:
                    pass
            if "-r" in item:
                try:
                    rValue = int(item[2:])
                except:
                    pass
            if "-v" in item:
                vertical = True
        if elements:
            try:
                print(line_gauss(elements, top, sigma, rValue, vertical))
                return True
            except:
                return False
        try:
            fileIn = argIn[0]
            fileOut = argIn[1]
        except:
            print("--< wrong parameters!")
            usage()
            return False
    else:
        usage()
    print("--< trying with: %s(%s), %s(%s)" % (fileIn, colored("fileIn", "cyan"),
                                               fileOut,colored("fileOut", "cyan")))
    parameters = read_parameters(fileIn)
    totalValues = []
    for param in parameters:
        values = get_gauss(elements=int(param[2]),
                           top=float(param[1]),
                           sigma=float(param[3]),
                           roundValue=2,
                           distName=param[0])
        totalValues += values
        totalValues.append("\n"+20*"-"+"\n")
    write_file(fileOut,
               totalValues,
               addNewline=True,
               response=True,
               removeSign=["(",")"])
    #args, value = zip(*values[1:]) #starts from 1 'cause 0 is name
    #draw_chart(args, value)


if __name__=="__main__":
    main(sys.argv[1:])

