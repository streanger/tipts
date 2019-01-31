import textwrap

def chunk_text(text, charsInLine):
    ''' text wrapper '''
    wrapper = textwrap.TextWrapper(width=charsInLine, break_long_words=False, replace_whitespace=False)
    out = wrapper.wrap(text)
    return out
    
    
if __name__ == "__main__":
    text = "someting here and there someting here and there someting here and there someting here and there someting here and there someting here and there someting here and there someting here and there someting here and there someting here and there someting here and there someting here and there someting here and there someting here and there someting here and there someting here and there someting here and there someting here and there someting here and there someting here and there someting here and there someting here and there someting here and there "
    
    out = chunk_text(text, 40)
    strContent = '\n'.join(out)
    print(strContent)