#this file contain some usefull things for 2.x and 3.x pythons

import sys


#python3.x
def get_time01():
    import subprocess   #put this on the top
    time = subprocess.getoutput("date +%X")
    return time

def get_time02():
    import datetime
    now = datetime.datetime.now().time()
    return now

def get_time03():
    import time
    now = time.strftime("%H:%M:%S")
    return now

def get_time04():
    import os
    f = os.popen("date +%X")
    now = f.read()[:-1]
    return now


if  sys.version[0] == "3":
    print("get time 01:", get_time01())
    print("get time 02:", get_time02())
    print("get time 03:", get_time03())
elif sys.version[0] == "2":
    print("get time 04", get_time04())



