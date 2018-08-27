import os
import sys
import time

def useless_stuff(loops):
    if loops < 6:
        loops = 8
    for x in range(loops):
        print(x, 'useless_stuff')
        time.sleep(0.5)
        if (loops - x) < 3:
            raise ValueError('something wrong happend...')
    return True


if __name__ == "__main__":
    args = sys.argv[1:]
    loops = int(args[0])
    useless_stuff(loops)