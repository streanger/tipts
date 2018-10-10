import os
import sys
import time

def useless_stuff(loops):
    some = []
    for x in range(loops):
        time.sleep(0.1)
        some.append(x)
    return True


if __name__ == "__main__":
    args = sys.argv[1:]
    loops = int(args[0])
    useless_stuff(loops)