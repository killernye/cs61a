def cascade0(n):
    print(n)
    if (n >= 10):
        cascade(n // 10)
        print(n)

def cascade1(n):
    """Another form of cascade. This one will be longer but more clear."""
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n : f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)



def fibonacci(n):
    """ Return the Nth fibonacci number."""
    assert type(n) == int and n >= 0, "N is not a non-negative integer."
    pre, cur, k = 1, 0, 0
    while k < n:
        pre, cur, k = cur, pre + cur, k + 1
    return cur


def count_partition(n, m):
    if n  == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partition(n-m, m)
        without_m = count_partition(n, m-1)
        return with_m + without_m
