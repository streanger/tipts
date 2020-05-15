import os
# import subprocess

def kill_proc_by_name(proc_name, force=False):
    ''' 
    -it will kill all processes with selected name
    -works on windows only
    -permissons required
    '''
    if force:
        os.system("taskkill -F /im {}".format(proc_name))
        # out = subprocess.getoutput(["taskkill", "-F", "/im", "{}".format(proc_name)])
    else:
        os.system("taskkill /im {}".format(proc_name))
        # out = subprocess.getoutput(["taskkill", "/im", "{}".format(proc_name)])
    return True
    
# kill_proc_by_name("chrome.exe")
if __name__ == "__main__":
    pythons_like = ['python.exe', 'pyw.exe', 'pythonw.exe']
    for python in pythons_like:
        kill_proc_by_name(python, True)


'''
todo:
-use subprocess to catch output
'''

