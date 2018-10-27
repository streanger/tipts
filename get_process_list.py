import wmi
import subprocess
import time

def timer(func):
    def f(*args, **kwargs):
        before = time.time()
        val = func(*args, **kwargs)
        after = time.time()
        print("func name: {}, elapsed time: {}s".format(func.__name__, after-before))
        return val
    return f

@timer
def get_process_list():
    '''return list of processes with using "wmi" python module'''
    c = wmi.WMI()
    tasks = c.Win32_Process()
    processList = [(process.Name, process.ProcessId) for process in tasks]
    processDict = {process.Name:process.ProcessId for process in tasks}
    processString = "\n".join([" ".join([process.Name, str(process.ProcessId)]) for process in tasks])
    return processString

@timer
def call_tasklist(filter=""):
    '''return list of processes with using "tasklist" command'''
    tasks = subprocess.check_output(["tasklist"])
    tasks = tasks.decode("utf-8", "ignore")
    processes = []
    for line in tasks.split("\n")[3:]:
        for key, element in enumerate(line.split()):
            if element.isdigit():
                processes.append(["_".join(line.split()[:key]), line.split()[key]])     #when join use " " or "_"
                break
    if filter:
        processes = [item for item in processes if item[0] == filter]
    processList = processes
    processDict = {item[0]:item[1] for item in processes}
    processString = "\n".join([" ".join(item) for item in processes])
    return processString
    
    
if __name__ == "__main__":
    # processes = get_process_list()
    processes = call_tasklist()
    print(processes)
    
