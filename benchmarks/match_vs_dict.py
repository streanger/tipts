
def match_func(key):
    match key:
        case 3: return 'this'
        case 2: return 'is'
        case 1: return 'code'
        case 0: return 'bench'
        case _: return 'mark'
        
def dict_func(key):
    data = {
        3: 'this',
        2: 'is',
        1: 'code',
        0: 'bench',
    }
    return data.get(key, 'mark')
    
# py -3.10 -m timeit -n 10000000 -s "from match_vs_dict import match_func" "match_func(3)"
# 10000000 loops, best of 5: 55.9 nsec per loop

# py -3.10 -m timeit -n 10000000 -s "from match_vs_dict import dict_func" "dict_func(3)"
# 10000000 loops, best of 5: 172 nsec per loop
