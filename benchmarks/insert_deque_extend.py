import timeit
import sys
from collections import deque

print(f'Python: {sys.version}')
number_of_items = 1000
print(f'      Number of items: {number_of_items}')

# List insert
start = timeit.default_timer()
table = [['a', 'b'] for _ in range(number_of_items)]
table.insert(0, ['header1', 'header2'])
end = timeit.default_timer()
print(f'     List insert time: {end - start}')

# Deque appendleft
start = timeit.default_timer()
table = deque([['a', 'b'] for _ in range(number_of_items)])
table.appendleft(['header1', 'header2'])
end = timeit.default_timer()
print(f'Deque appendleft time: {end - start}')

# List extend
start = timeit.default_timer()
table = [['a', 'b'] for _ in range(number_of_items)]
table = [['header1', 'header2']] + table
end = timeit.default_timer()
print(f'     List extend time: {end - start}')


"""
Python: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]

      Number of items: 1000
     List insert time: 0.00015769899982842617
Deque appendleft time: 0.00019275800150353462
     List extend time: 0.00017809200107876677

      Number of items: 10000
     List insert time: 0.002475544999470003
Deque appendleft time: 0.0033537110011820914
     List extend time: 0.0026421820002724417

      Number of items: 100000
     List insert time: 0.02852922199963359
Deque appendleft time: 0.021867479999855277
     List extend time: 0.023693721999734407

      Number of items: 1000000
     List insert time: 0.2902119969985506
Deque appendleft time: 0.3424597390003328
     List extend time: 0.2875185020002391

      Number of items: 10000000
     List insert time: 2.9946338569989166
Deque appendleft time: 3.287583455999993
     List extend time: 3.591648511999665
"""
