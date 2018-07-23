#!/usr/bin/python3
from sys import argv, exit

def print_ascii(start, stop):
    for sign in range(int(start), int(stop)):
        print(chr(sign), end="")
    print()

if __name__ == "__main__":
    args = argv[1:]
    if not args:
        print_ascii(12345, 13000)
        exit()
    try:
        start, stop = args[0].split("-")
        print_ascii(start, stop)
    except:
        print("wrong args!\nusage example:\n\tpython3 ascii.py 500-1000\n\t./ascii.py 500-1000")
