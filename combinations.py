#all combinations of two elements from two lists
import itertools
import termcolor

a = ["some", "thing", "strange"]
b = ["10", "20", "30"]

colors = list(termcolor.COLORS)
on_colors = list(termcolor.HIGHLIGHTS)

def all_products(a, b):
    return list(itertools.product(a, b))

#print(all_products(a, b))
#print(all_products(colors, on_colors))

for color, on_color in all_products(colors, on_colors):
    print(termcolor.colored("this is very example of the text -> %s %s" % (color, on_color), color=color, on_color=on_color))
