def rotate(sign, number):
    if ord(sign) + number >= 0:
        return chr(ord(sign)+number)
    else:
        return sign

for x in range(-10,10):
    print(x, rotate('l', x))

