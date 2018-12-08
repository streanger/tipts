
some = [11, 12, 13, 15, 17, 18, 19, 22, 24, 25, 26, 29]

def extract_series(data):
    ''' find series of number and extract them as subslist '''
    pairs = []
    pair = []
    for key, value in enumerate(data):
        if not pair:
            pair.append(value)
        else:
            if value - pair[-1] == 1:
                pair.append(value)
            else:
                pairs.append(pair)
                pair = [value]
    if pair:
        pairs.append(pair)
    return pairs
    
    
out = extract_series(some)
# print(out)
for item in out:
    print(item)
    
# updated 08.12.18, 20:28
listOfTuples = [(11, 2), (12, 2), (13, 2), (15, 3), (16, 3), (18, 4), (19, 4), (20, 4), (22, 5)]

def extract_tuple_series(data, centerOnly):
    ''' find series of number and extract them as subslist '''
    pairs = []
    pair = []
    for key, (value, second) in enumerate(data):
        if not pair:
            pair.append((value, second))
        else:
            if value - pair[-1][0] == 1:
                pair.append((value, second))
            else:
                pairs.append(pair)
                pair = [(value, second)]
    if pair:
        pairs.append(pair)
    if centerOnly:
        return [item[len(item)//2] for item in pairs]
    else:
        return pairs
        
out = extract_tuple_series(listOfTuples, True)
print("center only:")
for item in out:
    print('  ' + str(item))
out = extract_tuple_series(listOfTuples, False)
print("series pairs:")
for item in out:
    print('  ' + str(item))
    
'''
todo:
-should work for list of tuples/list with any size, not just with two elements
'''
