#cut list or string to small things
def cut_thing(thing, n):
    return [thing[x:x+n] for x in range(0, len(thing), n)]

#some = "this very thing"
#print(cut_string(some, 2))
#other = [1,2,3,4,5,6]
#print(cut_string(other,3))
