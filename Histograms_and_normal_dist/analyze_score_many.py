import os
import sys
import math
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pylab import savefig
import numpy as np
import random

def script_path():
    current_path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(current_path)
    return current_path
    
    
def read_file(file):
    with open(file, "r") as f:
        # this is specified for many data in one line, with coma as delimiter
        content = [item.split(',') for item in f.read().splitlines()]
    return content
    
    
def get_var_name(var):
    ''' won't work in function '''
    return [ k for k,v in locals().items() if v == var][0]
    
    
def just_draw(data, title):
    plt.plot(data, linewidth=1)
    plt.ylabel("y value")
    plt.xlabel("x value")
    plt.grid()
    x1,x2,y1,y2 = plt.axis()
    if max(data) < 1000:
        y2 = 1000
    plt.axis((x1,x2,y1,y2))
    plt.suptitle(title)
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')       #full window
    # plt.savefig(title.split('.')[0] + "_max.png")
    if 1:
        plt.show()
        plt.close()
    return True
    
    
def draw_hist(many_data, title):
    ''' put list of data to plot, as many_data variable '''
    # bins = np.linspace(0, 1000, 100)        # last parameter is width of columns
    bins = np.linspace(0, 1000, 200)        # last parameter is width of columns
    colors = []
    hist_number = len(many_data)
    probability = False
    for key, (file, data) in enumerate(many_data):
        cmap = plt.get_cmap('jet')
        current_color = cmap(key/hist_number)
        colors.append(current_color)
        plt.hist(data, bins, alpha=0.5, histtype='bar', ec='black', density=probability, label='this', color=current_color)

    cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']
    if probability:
        plt.ylabel('Probability')
    else:
        plt.ylabel('Elements')
    plt.xlabel('Score')
    
    #create legend
    handles = [Rectangle((0,0),1,1,alpha=0.5,color=c,ec="k") for c in colors]
    # labels= ["histogram: {}".format(key) for key, _ in enumerate(colors)]
    labels= ["{}: {}".format(key, many_data[key][0]) for key, _ in enumerate(colors)]       # make it more clear
    plt.legend(handles, labels)
    
    plt.suptitle(title)
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')       #full window
    # plt.savefig(title.split('.')[0] + "_max.png")
    if True:
        plt.show()
        plt.close()
    return True
    
    
if __name__ == "__main__":
    script_path()
    args = sys.argv[1:]
    files = [item for item in os.listdir() if item.endswith('.txt')]
    many_data = []
    for file in files:
        data = read_file(file)
        max_data = sorted([float(max(item)) for item in data])      # sorted is not needed(only for just_draw function)
        # just_draw(max_data, file)                                 # single one
        # draw_hist([max_data], file)                               # single one
        many_data.append((file, max_data))
        
    # draw all data in one chart
    draw_hist(many_data, 'some title here')
    
