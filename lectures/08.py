def gcd(m, n):
    """Returns the largest k that divides both m and n.

    k, m, n are all positive integers.

    >>> gcd(12, 8)
    4
    >>> gcd(16, 12)
    4
    >>> gcd(16, 8)
    8
    >>> gcd(2, 16)
    2
    >>> gcd(5, 5)
    5
    """
    if m % n == 0:
        return n
    if m < n:
        return gcd(n, m)
    else:
        return gcd(m-n, n)

def make_adder(n):
    return lambda k: n + k


def curry2(f):
    """2 means f takes in 2 arguments."""
    return lambda x: lambda y: f(x, y)

def trace1(fn):
    """Returns a version of fn that first prints before it is called.

    fn - a function of 1 argument
    """
    def traced(x):
        print('Calling', fn, 'on argument', x)
        return fn(x)
    return traced

@trace1
def square(x):
    return x * x

@trace1
def sum_square_up_to(n):
    k = 1
    total = 0
    while k <= n:
        total, k = total + square(k), k + 1
    return total


def horse(mask):
    horse = mask
    def mask(horse):
        return horse
    return horse(mask)

mask = lambda horse: horse(2)
