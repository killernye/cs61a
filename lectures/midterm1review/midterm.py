def is_fib(n):
    """Returns True if n is a fibonacci number,
    else False

    >>> is_fib(8)
    True
    >>> is_fib(9)
    False
    """
    cur, next = 0, 1
    while cur < n:
        cur, next = next, cur + next
    return cur == n


def is_ascending(n):
    """Returns True if the digits of N are in ascending order.

    >>> is_ascending(321)
    True
    >>> is_ascending(123)
    False
    >>> is_ascending(4432221)
    True
    >>> is_ascending(5492)
    False
    >>> is_ascending(5420)
    True
    """
    smallest = 0
    while n > 0:
        last, n = n % 10,  n // 10
        if smallest > last:
            return False
        smallest = last
    return True

def count_one(n):
    """Counts the number of 1s in the digits of n.

    >>> count_one(7007)
    0
    >>> count_one(123)
    1
    >>> count_one(161)
    2
    >>> count_one(1)
    1

    if n < 10:
        if n == 1:
            return 1
        else:
            return 0
    else:
        all_but_last, last = n // 10, n % 10
        if last == 1:
            return count_one(all_but_last)  + 1
        return count_one(all_but_last)
    """
    res = 0
    while n > 0:
        if n % 10 == 1:
            res += 1
        n //= 10
    return res

def total_ones(n):
    """Returns number of 1s in the digits of all numbers from 1 to n.

    >>> total_ones(10)
    2
    >>> total_ones(15)
    8
    >>> total_ones(21)
    13
    """
    k, count = 1, 0
    while k <= n:
        count, k = count + count_one(k), k + 1
    return count

def make_mod(n):
    """Returns a function that takes an argument x.
    That function will return x modulo n.

    >>> mod_7 = make_mod(7)
    >>> mod_7(3)
    3
    >>> mod_7(41)
    6
    """
    def mod(x):
        return x % n
    return mod

def foo(x):
    """Translates the following lambda expression into def statement.
    lambda x: lambda y: lambda z: x + y * z
    """
    def f(y):
        def g(z):
            return x + y * z
        return g
    return f

def map_mut(f, L):
    """Mutatively maps f onto each element in L.

    >>> L = [1, 2, 3, 4]
    >>> map_mut(lambda x: x**2, L)
    >>> L
    [1, 4, 9, 16]
    """
    for i in range(len(L)):
        L[i] = f(L[i])
