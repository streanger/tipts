from sympy import *
from sympy.solvers.solveset import linsolve


if __name__ == "__main__":
    # equation -->  ln(p) = A - B/(T-C)
    unknows = ['A', 'B', 'C']
    A, B, C = symbols('A B C')
    
    pairs = [(1, 1), (4, 4), (9, 9)]
    
    equations = ['A - B/({}-C) - ln({})'.format(T, p) for (T, p) in pairs]
    equations = [eval(item) for item in equations]              # think of ast
    print("equations:\n\t{}".format(equations))
    solution = solve(equations, [A, B, C])
    # solution = linsolve(equations, [A, B, C])                 # think of that
    
    print("solution:\n\t{}".format(solution))
    for key, item in enumerate(solution[0]):
        print("{}: {}".format(unknows[key], item.round(4)))
        
'''
useful stuff:
    https://stackoverflow.com/questions/31547657/how-can-i-solve-system-of-linear-equations-in-sympy
    
'''
