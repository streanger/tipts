import numpy as np
import sys
import os

def script_path():
    '''set current path to script path, and return it as string'''
    current_path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(current_path)
    return current_path
    
    
def simple_write(file, data):
    '''simple_write data to .txt file, with specified data'''
    with open(file, "w") as f:
        f.write(str(data) + "\n")
        f.close()
    return True
    
    
def get_normal_dist(mu, sigma, elements):
    return np.random.normal(mu, sigma, elements)
    
    
if __name__ == "__main__":
    current_path = script_path()
    # mu, sigma, elements = 300, 15, 1000
    # mu, sigma, elements = 600, 20, 1000
    mu, sigma, elements = 800, 30, 1000
    normal_data = get_normal_dist(mu, sigma, elements)
    normal_to_write = '\n'.join([str(item) for item in normal_data])
    simple_write('normal_data03.txt', normal_to_write)
    
    