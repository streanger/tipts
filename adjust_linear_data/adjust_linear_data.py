

def adjust_linear_data(expected_data, current_data):
    '''we want to find a and b coeff of linear translation current_data to expected_data
    formula:
        ((item - b_current)/a_current)*a_expected + b_expected
        ((item/a_current - b_current/a_current)*a_expected + b_expected
        ((item*(a_expected/a_current) - b_current*(a_expected/a_current)) + b_expected
    '''
    
    # coeffs of expected_data
    a_expected, b_expected = linreg(Y=expected_data)
    
    # coeffs of current_data
    a_current, b_current = linreg(Y=current_data)
    
    # calc a, b
    a = (a_expected/a_current)
    b = b_expected - b_current*(a_expected/a_current)
    
    return a, b
    
    
def linreg(X=None, Y=None):
    """calculate trend line -> 'a' & 'b' factories"""
    if X is None:
        X = [x for x in range(len(Y))]
    N = len(X)
    Sx = Sy = Sxx = Syy = Sxy = 0.0
    for x, y in zip(X, Y):
        Sx = Sx + x
        Sy = Sy + y
        Sxx = Sxx + x*x
        Syy = Syy + y*y
        Sxy = Sxy + x*y
    det = Sxx * N - Sx * Sx
    return (Sxy * N - Sy * Sx)/det, (Sxx * Sy - Sx * Sxy)/det
    
    
if __name__ == "__main__":
    expected_data = [2, 4, 6, 8, 10, 12]
    current_data = [4, 7, 10, 13, 16, 19]
    
    a, b = adjust_linear_data(expected_data, current_data)
    print(a, b)
