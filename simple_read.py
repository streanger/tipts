import codecs
def simple_read(file):
    '''simple_read data from specified file'''
    with codecs.open(file, "r", encoding="utf-8", errors='ignore') as f:
        content = f.read().splitlines()
    return content
