def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    st_dis = abs(street(a) - street(b))
    ave_dis = abs(avenue(a) - avenue(b))
    return st_dis + ave_dis


def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    def is_perfect_square(n):
        i = 1
        while n > 0:
            n, i = n - i, i + 2
        return n == 0

    def perfect_square(n):
        left, right, mid = 0, n, n//2
        while True:
            if mid * mid  == n:
                return mid
            elif mid * mid > n:
                left, right = left, mid - 1
            else:
                left, right = mid + 1, right
            mid = (left + right) // 2

    res = []
    for i in s:
        if is_perfect_square(i):
            res.append(perfect_square(i))
    return res
