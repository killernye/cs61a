def fibonacci(n):
    """Return the nth fibonacci number.
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(9)
    34
    """
    pre_two = 0
    pre_one = 1

    if n == 0:
        return 0
    elif  n == 1:
        return 1
    else:
        i = 2 # the current position of fib number
        cur = pre_two + pre_one
        while i < n:
            pre_two = pre_one
            pre_one = cur
            cur = pre_two + pre_one
            i = i + 1
        return cur

from math import pi, sqrt

def area(r, shape_constant = 1):
    """ return the area of the length based on shape_constant"""
    assert r > 0, 'A length must be positive.'
    return shape_constant * r * r

def  area_square(r):
    return area(r, 1)

def area_circle(r):
    return area(r, pi)

def area_hexagon(r):
    return area(r, 3 * sqrt(3) / 2)


def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def summation(n, term):
    """Sum the first N terms of a sequence.

    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def sum_naturals(n):
    """Sum the first N natural numbers.

    >>> sum_naturals(5)
    15
    """
    return summation(n, identity)


def sum_cubes(n):
    """Sum the first N cubes of natural numbers.

    >>> sum_cubes(5)
    225
    """
    return summation(n, cube)

def make_adder(n):
    """Return a function that takes one arguement K and return K + N.

    >>> add_three = make_adder(3)
    >>> add_three(2)
    5
    """
    def adder(k):
        return n + k
    return adder
