import random
import numpy as np
import time

def execute_decorator(func):
    def f(*args, **kwargs):
        before = time.time()
        val = func(*args, **kwargs)
        total = round((time.time() - before), 9)
        print("--> <{}> finished in {}[s]".format(func.__name__, total))
        return val
    return f
    
    
@execute_decorator
def array_cross(m, out_type):
    ''' m -> two dimension numpy array; out_type -> 'any', 'all', try also with max/min 
        function checks if there are non-zero values in the cross of the points '''
        
    data_hor = [m[key,:] for key in range(m.shape[0])]                          # horizontal
    data_hor = [[[line[1]]] + (np.take(line, [[key-1, key+1] for key in range(1, line.size-1)])).tolist() + [[line[line.size-2]]] for line in data_hor] # right/left values
    data_hor = np.matrix(data_hor)
    
    data_ver = [m[:,key] for key in range(m.shape[1])]                          # vertical
    data_ver = [[[line[1]]] + (np.take(line, [[key-1, key+1] for key in range(1, line.size-1)])).tolist() + [[line[line.size-2]]] for line in data_ver] # up/down values
    data_ver = np.matrix(data_ver).transpose()
    
    out_matrix = data_hor + data_ver                                            # all values in the cross
    out = [out_matrix[key,:] for key in range(out_matrix.shape[0])]
    if out_type == 'any':
        out = [[any(dot) for dot in np.array(line)[0]] for line in out]         # get boolean or int values -> max(dot); any(dot); all(dot)
    else:
        out = [[all(dot) for dot in np.array(line)[0]] for line in out]         # get boolean or int values -> max(dot); any(dot); all(dot)
        
    out = np.array(out).astype(int)
    return out
    
    
if __name__ == "__main__":
    # timing example
    m = np.array([[random.choice((0, 1)) for x in range(200)] for y in range(200)])
    for x in range(5):
        out = array_cross(m, 'any')
        
    # output example
    m = np.array([[random.choice((0, 1)) for x in range(25)] for y in range(25)])
    out = array_cross(m, 'any')
    print("\noriginal data:\n\n{}\n\noutput data:\n\n{}\n".format(m, out))