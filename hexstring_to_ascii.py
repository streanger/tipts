#!/usr/bin/python3
import sys
import os

def script_path():
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)  #it seems to be quite important
    return path

def chunks(l, n):
    some = [(l[i:i + n]) for i in range(0, len(l), n)]
    return some

def hex_ascii(hexString):
    if " " in hexString:
        hexes = hexString.split()
    else:
        hexes = chunks(hexString, 2)
    return "".join([chr(int("0x"+item,16)) for item in hexes])

def ascii_hex(asciiString):
    hexString = [("0"*(4-len(hex(ord(item)))) + hex(ord(item))[2:]).upper() for item in asciiString]
    prefix = " ".join(["0x" + item for item in hexString])
    return " ".join(hexString), "".join(hexString), prefix


if __name__ == "__main__":
    ask = input("hex_to_ascii(1) or ascii_to_hex(2)?\n")
    if ask == "1":
        hexToAscii = True
    elif ask == "2":
        hexToAscii = False
    else:
        print("wrong choice. Exiting...")
        sys.exit()
    if hexToAscii:
        some = input("podaj hexstring:\n")
    else:
        some = input("podaj asciistring:\n")
    while some[0] != "q":
        if hexToAscii:
            print(hex_ascii(some))
            some = input("podaj hexstring:\n")
        else:
            print(ascii_hex(some))
            some = input("podaj asciistring:\n")
