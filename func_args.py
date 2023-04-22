"""
bare asterisk in function definition:
    https://stackoverflow.com/questions/14301967/bare-asterisk-in-function-parameters
    https://peps.python.org/pep-3102/
    
forward slash in function definition:
    https://stackoverflow.com/questions/24735311/what-does-the-slash-mean-when-help-is-listing-method-signatures
    
"""

def thing(a, b, /, x, y, *, z=4):
    print(a, b, x, y, z)
    
    
# thing(1, 2, 3, 4, 5)  # TypeError: thing() takes 4 positional arguments but 5 were given
# thing(a=1, b=2, x=3, y=4, z=5)  # TypeError: thing() got some positional-only arguments passed as keyword arguments: 'a, b'
thing(1, 2, x=3, y=4, z=5)  # works fine
thing(1, 2, 3, y=4, z=5)  # works fine
thing(1, 2, 3, 4, z=5)  # works fine

"""
a, b - can be postional args only
x, y - can be both positional or key-value args
z - can be only key-value args
"""
