''' check if string contains only specified characters; timing '''
import time
import re


def timer(func):
    def f(*args, **kwargs):
        before = time.time()
        val = func(*args, **kwargs)
        total = round((time.time() - before), 4)
        print("func: {} -->  elapsed time:  {}s".format(func.__name__.ljust(20), total))
        return val
    return f
    
    
@timer
def check_with_regex(data, chars):
    reg = re.compile('^[0-1]*$')
    if reg.findall(data):
        return True
    else:
        return False
    
    
@timer
def check_with_replace(data, chars):
    for c in chars:
        data = data.replace(c, '')
    if not data:
        return True
    else:
        return False
        
        
if __name__ == "__main__":
    count = 10000000
    bad = 'this is very false 0 1 10 data'*count
    good = '11001010001010100101'*count
    
    # test bad
    check_with_regex(bad, '01')
    check_with_replace(bad, '01')
    
    # test good
    check_with_regex(good, '01')
    out = check_with_replace(good, '01')
