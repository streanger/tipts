#!/usr/bin/python3
import matplotlib.pyplot as plt


def straight_line(data):
    #works ok if get data
    if not data:
        return []
    b = data[0]
    a = (data[-1] - b)/(len(data)-1)
    newData = [a*x + b for x, val in enumerate(data)]
    return newData

def close_contour(data):
    #no falling down until the end
    lastMax = list(enumerate(data))[0]
    falling = False
    newData = data + []
    for key, item in enumerate(data):
        if not key:
            continue
        if item > lastMax[1]:       #> or >=
            if falling:
                #join peaks -> draw arc or straight line
                element = straight_line(data[lastMax[0]:key+1])
                newData = newData[:lastMax[0]] + element + newData[key+1:]
                lastMax = key, item
                falling = False
            lastMax = key, item
        else:
            falling = True
        #print("falling: {}, lastMax: {}".format(falling, lastMax))
    return newData

def draw_plot(data):
    plt.plot(data, color="blue", marker='o', markersize='4', linewidth=1)
    plt.show(data)
    return True

if __name__ == "__main__":
    data = [-(x+2)**2+40 for x in range(-5,5)]
    data = data[:4] +  [28,24,22,25,26] + data[4:]      #one set of data

    #data = [1,2,4,5,6,4,3,5,6,7,9,12,14,10,7,5,8,12,15,13,8,5,2]   #another example of data
    print(len(data), data)
    draw_plot(data)

    newData = close_contour(close_contour(data)[::-1])[::-1]        #make it 2 times -> data & reveresed data; need for develop - think of decorator?
    print(len(newData), newData)
    draw_plot(newData)
