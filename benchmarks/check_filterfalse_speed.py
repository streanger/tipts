import itertools
import random
import timeit


def check(item):
    if type(item) is int:
            return True
    return False
    
def check_not(item):
    if type(item) is int:
            return False
    return True
    
def generate_data(n):
    for x in range(n):
        if random.randrange(2):
            yield random.random()
        else:
            yield random.randrange(10)
            
def list_comp_filter(data):
    return [item for item in data if not type(item) is int]
    
def itertools_filterfalse(data):
    return list(itertools.filterfalse(check_not, data))
    
    
# data = generate_data(1_000_000)
data = generate_data(1_000)
list_comp_time = timeit.timeit(lambda: list_comp_filter(data), number=1)
itertools_filterfalse_time = timeit.timeit(lambda: itertools_filterfalse(data), number=1)
print('list_comp: {}'.format(list_comp_time))
print('itertools_filterfalse: {}'.format(itertools_filterfalse_time))
