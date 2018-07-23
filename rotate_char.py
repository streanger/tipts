#!/usr/bin/python3
import string

def rotate(sign, number):
    #rotate by all ascii
    if ord(sign) + number >= 0:
        return chr(ord(sign)+number)
    else:
        return sign

def rotate(seq, sign, number):
    #specified sequence of chars
    number += seq.index(sign)
    number = number%len(seq)
    return seq[number]

def rotate_string(someString, number):
    ascii_lower = string.ascii_lowercase
    ascii_upper = string.ascii_uppercase
    stringOut = ""
    for item in someString:
        if item in ascii_lower:
            stringOut += rotate(ascii_lower, item, int(number))
        elif item in ascii_upper:
            stringOut += rotate(ascii_upper, item, int(number))
        else:
            stringOut += item
    return stringOut


someString = "Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh"
print(rotate_string(someString, -13))
