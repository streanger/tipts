'''
======================
3D surface (color map)
======================

Demonstrates plotting a 3D surface colored with the coolwarm color map.
The surface is made opaque by using antialiased=False.

Also demonstrates using the LinearLocator and custom formatting for the
z axis tick labels.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import random


def plot_figure(data=[], subtitle=""):    
    if True:
        data = np.matrix(data)
        data = data.transpose()     #swap axes; its important in 3d view
        ySize, xSize = data.shape
        #print(ySize, xSize)

        X = np.arange(0, xSize, 1)
        Y = np.arange(0, ySize, 1)
        X, Y = np.meshgrid(X, Y)
        Z = data
    else:
        # Make data.
        X = np.arange(-2, 2, 0.25)      #range and step => 4/0.25 = 16 points
        Y = np.arange(-2, 2, 0.25)
        X, Y = np.meshgrid(X, Y)
        R = np.sqrt(X**2 + Y**2)
        #Z = np.cos(2*R)

        #Z = np.zeros((16, 16))
        Z = np.matrix([[random.randrange(x+y+1) for x in range(16)] for y in range(16)])

    
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=True)

    # Customize the z axis.
    #ax.set_zlim(-1.01, 1.01)
    ax.set_zlim(0, 25)
    ax.zaxis.set_major_locator(LinearLocator(10))
    #ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%d'))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    
    #make plot zoomed
    plt.suptitle(subtitle)
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')       #full window
    plt.show()
    return True

if __name__ == "__main__":
    data = [[1,1,1,1,2,2,2,3,2,2,1,1,1],
            [1,1,2,2,3,5,5,6,5,3,1,1,1],
            [1,1,2,13,5,7,8,8,7,5,2,1,1],
            [1,1,12,13,5,17,18,8,7,5,2,1,1],
            [1,1,2,3,15,17,18,18,7,5,2,1,1],
            [1,1,2,3,5,16,17,17,16,4,2,1,1],
            [1,1,2,2,3,5,5,16,5,3,11,1,1],
            [1,1,1,1,2,2,2,3,2,2,1,1,11]]
    '''
    data = [[1,2,3],
            [1,2,1],
            [1,1,1]]
    '''
     
    plot_figure(data)


    
