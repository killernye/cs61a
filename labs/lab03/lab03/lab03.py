def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    a, b = max(a, b), min(a, b)
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n == 1:
        return 1
    if n % 2 == 0:
        return hailstone(n // 2) + 1
    else:
        return hailstone(n * 3 + 1) + 1


def factorial(n, res_except_n):
    res_except_n = 1
    while n > 0:
        res_except_n, n = res_except_n * n, n - 1
    return res_except_n


def gcd_iter(a, b):
    """Return the largest common divisor of two positive integers A and B by iterative method.

    >>> gcd_iter(12, 8)
    4
    >>> gcd_iter(15, 15)
    15
    >>> gcd_iter(3, 15)
    3
    """
    a, b = max(a, b), min(a, b)

    while a % b != 0:
        a, b = b, a % b
    return b
