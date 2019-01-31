import textwrap

def chunk_text(text, charsInLine):
    ''' text wrapper '''
    wrapper = textwrap.TextWrapper(width=charsInLine, break_long_words=False, replace_whitespace=True, drop_whitespace=True)
    out = wrapper.wrap(text)
    return out
    
    
if __name__ == "__main__":
    text = 'This is very strange thing. Your spy bot is just went into the enemy space ship.\nYour mission is to get the secret data and escape from the hostile ship.\nGood luck...'
    text = text.splitlines()        # need to use it before
    
    # out = '\n'.join(['\n'.join(chunk_text(item, 22)) for item in text])
    out = '\n '.join(['\n'.join(chunk_text(item, 23)) for item in text])        # space added after true newline
    # print(out)
    print(repr(out))
    
