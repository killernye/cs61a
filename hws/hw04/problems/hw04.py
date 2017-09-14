HW_SOURCE_FILE = 'hw04.py'

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)


def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    if n <= 3:
        return n
    pre1, pre2, pre3, k = 3, 2, 1, 4
    while k < n:
        pre1, pre2, pre3, k = pre1 + 2*pre2 + 3*pre3, pre1, pre2, k + 1
    return pre1 + 2*pre2 + 3*pre3

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True

iteration version:
    direction = 1
    k = 1
    res = 0
    while k < n:
        res += direction
        if has_seven(k) or k % 7 == 0:
            direction *= -1
        k += 1
    return res + direction

helper version:
    def helper(k, direction, res):
        if k == n:
            return res + direction
        else:
            if has_seven(k) or k % 7 == 0:
                return helper(k+1, -direction, res + direction)
            return helper(k+1, direction, res + direction )
    return helper(1,1,0)
"""
    if n < 8:
        return n
    else:
        if has_seven(n-1) or (n-1) % 7 == 0:
            return pingpong(n-2)
        return pingpong(n-1) * 2 - pingpong(n-2)

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    k = 0
    while pow(2, k) <= amount:
        k += 1
    k = k - 1
    biggest_coin = pow(2, k)
    def count(amount, biggest_coin):
        if biggest_coin == 0:
            return 0
        elif amount == 0:
            return 1
        elif amount < 0:
            return 0
        else:
            return count(amount, biggest_coin//2) + count(amount - biggest_coin, biggest_coin)
    return count(amount, biggest_coin)






###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True

    return lambda n: (lambda f, v: f(f, v))(lambda f, v): 1 if v == 1 else mul(v, f(f, sub(v, 1))) , n)
    """
    return lambda n: (lambda f, v: f(f, v))(lambda f, v: 1 if v == 1 else mul(v, f(f, sub(v, 1))), n) 
