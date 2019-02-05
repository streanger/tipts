import pprint
import psutil

def get_proc_files():
    for proc in list(psutil.process_iter()):
        try:
            flist = proc.open_files()
            print(str(proc.pid).ljust(5), proc.name().ljust(25), flist)
        except:
            pass
    return True
    
    
if __name__ == "__main__":
    procList = list(psutil.process_iter())
    data = procList[9].connections()         # looks nice
    pprint.pprint(data)

    # todo -> return instead of print inside
    get_proc_files()