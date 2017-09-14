def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)


def count(f):
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

def memo(f):
    cache = {}
    def memorized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memorized

def count_frames(f):
    def counted(n):
        counted.open_count += 1
        if counted.open_count > counted.max_count:
            counted.max_count = counted.open_count
        result = f(n)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted

@count
def divides(k, n):
    return n % k == 0

def factors(n):
    total = 0
    for k in range(1, n+1):
        if divides(k, n):
            total += 1
    return total

from math import sqrt

def factors_fast(n):
    total = 0
    sqrt_n = sqrt(n)
    k = 1
    while k < sqrt_n:
        if divides(k, n):
            total += 2
        k += 1
    if k*k == n:
        total += 1
    return total

@trace
def exp(b, n):
    if n == 0:
        return 1
    else:
        return b * exp(b, n-1)
