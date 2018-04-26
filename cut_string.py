
#cut list or string to small things

def cut_string(thing, n):
    return [thing[x:x+n] for x in range(0, len(thing), n)]

some = "this very thing"
print(cut_string(some, 2))
