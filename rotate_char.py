def rotate(sign, number, direction):
    if direction:
        return chr(ord(sign)+number)
    else:
        return chr(ord(sign)-number)

#print(rotate('a', 10, True))

