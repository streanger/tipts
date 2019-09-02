import sys
import time


def fill_line(value):
    '''value -> int from 0-100'''
    number = 50
    line = '-'*number
    point = round((value*number)//100)
    out = line.replace('-', '>', point)
    return out
    
    
if __name__ == "__main__":
    for x in range(100):
        line = fill_line((x+1)) + ' {}%'.format(x+1)
        print('{}'.format(line), end='\r', flush=True)
        time.sleep(0.03)
    print()
