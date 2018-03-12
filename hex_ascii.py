import textwrap as tw

def hex_ascii(data):
    return "".join([chr(int("0x"+x,16)) for x in tw.wrap(data,2)])
