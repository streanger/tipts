import psutil
import time
import subprocess

def used_memory():
    '''returns percentage memory usage, current used & total memory in GB'''
    memory = psutil.virtual_memory()
    used = memory.used
    total = memory.total
    usedGB = round(used/1024/1024)
    totalGB = round(total/1024/1024)
    percentage = round((used/total)*100, 2)
    return percentage, usedGB, totalGB

def last_boot():
    bootTime = psutil.boot_time()
    now = time.time()
    hoursSinceBoot = round((now - bootTime)/3600, 2)       #in hours
    daysSinceBoot = round(hoursSinceBoot/24, 2)
    return daysSinceBoot

def tasklist():
    '''return list of processes with using "tasklist" command'''
    tasks = subprocess.check_output(["tasklist"])
    tasks = tasks.decode("utf-8", "ignore")
    processes = []
    for line in tasks.split("\n")[3:]:
        for key, element in enumerate(line.split()):
            if element.isdigit():
                processes.append(["_".join(line.split()[:key]), line.split()[key]])     #when join use " " or "_"
                break
    processList = processes
    processDict = {item[0]:item[1] for item in processes}
    processString = "\n".join([" ".join(item) for item in processes])
    return processDict

def get_users():
    out = psutil.users()
    #prepare data if needs
    return out

def services():
    winServices = psutil.win_service_iter()
    return winServices

def stuff():
    sinceBoot = last_boot()
    print("\n\t>> last boot was: {} [days] ago <<\n".format(sinceBoot))

    users = get_users()
    print(users)
    
    # '''
    while True:
        time.sleep(1)
        percentUsage, usedGB, totalGB = used_memory()
        print("memory usage: {} [%]\t\t{}/{} [MB]".format(percentUsage, usedGB, totalGB))
    # '''
    
if __name__ == "__main__":
    # tasks = tasklist()
    # pythonPid = int(tasks["python.exe"])
    # print("pythonPid: {}".format(pythonPid))
    # pyProcess = psutil.Process(pythonPid)
    # variables = pyProcess.environ()
    stuff()
    
