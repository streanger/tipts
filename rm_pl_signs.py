#!/usr/bin/python3

def rm_pl_signs(plString):
    plSigns = {'ą':'a', 'ć':'c', 'ę':'e', 'ł':'l', 'ń':'n', 'ó':'o', 'ś':'s', 'ź':'z', 'ż':'z'}
    for key, val in plSigns.items():
        if key in plString:
            plString = plString.replace(key, val)
    return plString

plString = "żółte słońce i śniada ćma, pomykają pomiędzy źdźbłami trawy"
converted = rm_pl_signs(plString)
print("polish string: {}".format(plString))
print("converted string: {}".format(converted))
