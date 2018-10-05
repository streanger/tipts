import time
import datetime

def time_template():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime("%Y-%m-%d %H:%M:%S"))
    startLine = 50*"-" + "\n\tstart time:\t" + date + "\n" + 50*"-"
    return startLine

def time_decorator(func):
    def f(*args, **kwargs):
        print(time_template())
        val = func(*args, **kwargs)
        return val
    return f

@time_decorator
def some_func(a, b):
    return a+b    

some_func(2, 2)