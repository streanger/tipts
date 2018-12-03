
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