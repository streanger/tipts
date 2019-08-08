import sys
import os
import random
import numpy as np

# draw hist
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pylab import savefig

# calc coefficient
from statistics import median


def script_path():
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    return path
    
    
def simple_write(file, s):
    '''simple_write data to .txt file, with specified string(s)'''
    with open(file, "w") as f:
        f.write(s)
        f.close()
    return True
    
    
def simple_read(file):
    '''simple_write data to .txt file, with specified string(s)'''
    with open(file, "r") as f:
        data = f.read().splitlines()
        f.close()
    return data
    
    
def generate_data(min_val, max_val, elements):
    # first = np.random.normal(mu, sigma, 200)
    data = np.random.normal(mu, sigma, 1000)
    return data
    
    
def calc_coefficient(first, second, min_val, max_val, level):
    '''
        first       -first data
        second      -second data
        min_val     -minimal limit of data
        min_val     -maximal limit of data
        level       -percent value of items between min_val and max_val
        
        
        todo:
            -do it for many data in a list [('title_01', data_01), ('title_02', data_02)]
            and then iter for each one
        
    '''
    dictio = {}
    manyData = [first, second]
    for key, (title, data) in enumerate(manyData):
        # calc a_coeff
        # range should be the value between min_val and max_val
        # steps = np.linspace(0.5, 2.0, 101)
        steps = np.linspace(0.7, 1.5, 10)
        allData = len(data)
        for step in steps:
            input(str(step) + ' press enter... ')
            bestRanges = []
            scaledData = step * data
            setData = list(set(scaledData))
            for element in setData:
                # print(len(setData))
                # for every element in list make range
                # than check how many items are inside
                # return the best value
                itemsInside = len([item for item in scaledData if (element <= item <= element + (max_val - min_val))])
                bestRanges.append((element, (itemsInside/allData)*100))
                # print((itemsInside/allData)*100)
            best = sorted(bestRanges, key=lambda x: x[1], reverse=True)[0][1]
            # print(best)
            if best > level:
                print('for step: {}, and element: {}, best value is: {}'.format(step, element, best))
                a_coeff = step
                break
            
        # calc b_coeff
        if True:
            # here we need to use scaledData
            # medianValue = median(data)
            medianValue = median(scaledData)
            print('{}. medianValue: {}'.format(key, medianValue))
            dictio[title] = {'a_coeff': a_coeff, 'b_coeff': (min_val + max_val)/2 - medianValue}
        
        
        
        # designate median value, to move histogram in the left-right direction
        # calc a parameter, to achieve specified level value(0-100%)
    return dictio
        
    first_A = 1.0
    first_B = 0.0
    second_A = 1.0
    second_B = 0.0
    return (first_A, first_B), (second_A, second_B)
    
    
def draw_hist(many_data, title):
    ''' for single data array/list
        for many data(in this case for two)
    '''
    

    ''' put list of data to plot, as many_data variable '''
    # bins = np.linspace(0, 1000, 100)        # last parameter is width of columns
    # bins = np.linspace(0, 1000, 200)        # last parameter is width of columns
    bins = np.linspace(0, 10, 200)          # last parameter is width of columns
    colors = []
    hist_number = len(many_data)
    probability = False
    
    for key, (file, data) in enumerate(many_data):
        cmap = plt.get_cmap('jet')
        current_color = cmap(key/hist_number)
        colors.append(current_color)
        plt.xticks(np.arange(0, 10, 0.5))   # is it in collision with bins??
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
    
    # generateMode = True
    generateMode = False
    
    
    if generateMode:
        # generate random data
        first = np.random.normal(3.6, 0.3, 2500)
        # second = np.random.normal(4.2, 0.4, 2500)
        second = np.concatenate((np.random.normal(4.2, 0.4, 2000), np.random.normal(4.8, 0.5, 500)))
        print(max(first), min(first))
        print(max(second), min(second))
        
        # store random data into file
        simple_write('data_01.txt', '\n'.join([str(item) for item in first]))
        simple_write('data_02.txt', '\n'.join([str(item) for item in second]))
        
    else:
        # read random data
        file_01 = 'data_01.txt'
        file_02 = 'data_02.txt'
        first = np.array([float(item) for item in simple_read('data_01.txt')])
        second = np.array([float(item) for item in simple_read('data_02.txt')])
        
        many_data = [(file_01, first), (file_02, second)]
        draw_hist(many_data, 'title')
        # show single hist
        
        # show double hist in one
        
        # show hist from combined data(arrays/lists are added)
        
        # calc_coefficient
        # do the job here
        dictio = calc_coefficient(('first', first), ('second', second), 3.2, 4.8, 80)
        print(dictio)
        input('contiue with this stuff? ')
        many_data = [(file_01, first * dictio['first']['a_coeff'] + dictio['first']['b_coeff']),
                     (file_02, second * dictio['second']['a_coeff'] + dictio['second']['b_coeff'])]
        # print(dictio)
        draw_hist(many_data, 'title')
        
        
'''
info:
    -why do i have to do this in my free time??
    -
    
'''
