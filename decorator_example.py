#!/usr/bin/python3
import time

def timer(func):
    def f(*args, **kwargs):
        before = time.time()
        val = func(*args, **kwargs)
        after = time.time()
        print("elapsed time: {}s".format(after-before))
        return val
    return f

@timer
def some_func(a, b):
    return a+b



print("sum of 10+15:", some_func(10, 15))
