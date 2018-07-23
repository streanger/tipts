#!/usr/bin/python3

some = [(1, 22), (2,34), (3, 15)]
def max_tuple_val(tuples, elementNo):
    return max(tuples, key=lambda x:x[elementNo])
print(max_tuple_val(some, 1))
