
prefixes = ('THIS: ', 'IS: ', 'SPARTA:')
text = 'THIS: THIS: IS: this is in fact subject'
text = 'IS: THIS: SPARTA:SPARTA:this is actually sparta'

def remove_prefixes(text, prefixes):
    """remove many prefixes in loop"""
    last = text
    while True:
        for prefix in prefixes:
            text = text.removeprefix(prefix)
        if last != text:
            last = text
        else:
            break
    return text
    
new = remove_prefixes(text, prefixes)
print(new)
