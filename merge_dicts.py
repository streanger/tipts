#!/usr/bin/python3

def merge_dicts(*dict_args):
    result = {}
    for d in dict_args:
        result.update(d)
    return result

dictio1 = dict(zip(["first" + str(x) for x in range(3)], [x for x in range(3)]))
dictio2 = dict(zip(["second" + str(x) for x in range(3)], [x**2 for x in range(3)]))


dictOut = merge_dicts(dictio1, dictio2)
print(dictOut)

# from python3.5
out = {**dictio1, **dictio2}
print(out)
