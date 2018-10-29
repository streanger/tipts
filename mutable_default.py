def foo(numbers=None):
    if numbers is None:
        numbers = []
    numbers.append(9)
    return numbers
