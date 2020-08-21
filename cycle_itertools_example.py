import itertools


data = itertools.cycle([1, 2, 3])
for x in range(10):
    item = next(data)
    print(x, item)
    
'''
-how cycle works
-you create object, which stores specified values and return next in turn
'''
