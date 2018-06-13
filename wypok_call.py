#!/usr/bin/python3

def nick_to_call():
    nicknames = input("put string of wypok nicnames:\n")
    if not nicknames:
        print("empty string...")
        return ""
    return " ".join(["@" + item + ":" for item in nicknames.split(", ")])

while (1):
    toCall = nick_to_call()
    print("toCall:\n", toCall)
