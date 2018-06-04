#!/usr/bin/python3
import numpy as np
from statistics import mean
import matplotlib.pyplot as plt


#some = np.arange(256)
#some = some.reshape((8,32))
some = np.random.rand(60,480)
#some = some.flatten(1)

def draw_chart(data):
    data_x = [key for key, val in enumerate(data)]
    plt.plot(data_x, data)
    plt.xlabel("pixels[n]")
    plt.ylabel("intensity[0-255]")
    plt.grid()
    plt.show()
    return True

def make_vector(someArray):
    #convert 2d, n-size array/matrix to 1d vector
    h = someArray.shape[0]
    someArray = someArray.flatten(1)
    print(h)
    return [mean(someArray[i:i+h]) for i in range(0,len(someArray),h)]

vector = make_vector(some)
#print(vector)
draw_chart(vector)
