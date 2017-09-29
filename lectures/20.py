class Link:
    """A linked list.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.first
    1
    >>> s.rest
    Link(2, Link(3))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({})'.format(self.first)
        else:
            return 'Link({}, {})'.format(self.first, repr(self.rest))

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 +  len(self.rest)

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value


s = Link(3, Link(4, Link(5)))
square = lambda x: x * x
odd = lambda x: x % 2 == 1

def extend_link(s, t):
    """Return a Link with elements of s followed  by those of t."""
    if s is Link.empty:
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))

def map_link(f, s):
    """Apply f to each element of s."""
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))

def filter_link(f, s):
    """Return a Link with elements of s for which f returns true."""
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        return filtered

def join_links(s, separator):
    """Return a string of all elements in s separated by separator."""
    if s is Link.empty:
        return ""
    elif s.rest is Link.empty:
        return str(s.first)
    else:
        return str(s.first) + separator + join_links(s.rest, separator)

def partitions(n, m):
    """Return a linked list of partitions of n & parts of up to m.
    Each partition is represented as a linked list."""
    if n == 0:
        return Link(Link.empty)
    elif n < 0 or m == 0:
        return Link.empty
    else:
        using_m = partitions(n-m, m)
        with_m = map_link(lambda p: Link(m, p), using_m)
        without_m = partitions(n, m-1)
        return extend_link(with_m, without_m)

def print_partitions(n, m):
    """Print the partitions of n using parts up to size m."""
    links = partitions(n, m)
    lines = map_link(lambda s: join_links(s, "+"), links)
    map_link(print, lines)

# Sets as unsorted sequences

def empty(s):
    return s is Link.empty

def contains(s, v):
    """Return true if set S contains value V as an element.

    >>> s = Link(1, Link(3, Link(2)))
    >>> contains(s, 2)
    True
    >>> contains(s, 5)
    False
    """
    if empty(s):
        return False
    elif s.first == v:
        return True
    else:
        return cotains(s.rest, v)

def adjoin(s, v):
    if contains(s, v):
        return s
    else:
        return Link(v, s)

def intersect(set1, set2):
    in_set2 = lambda v: contains(set2, v)
    return filter_link(in_set2, set1)

def union(set1, set2):
    not_in_set2 = lambda v: not contains(set2, v)
    set1_not_set2 = filter_link(not_in_set2, set1)
    return extend_link(set1_not_set2, set2)

# Sets as sorted sequences

def empty(s):
    return s is Link.empty

def contains(s, v):
    """Return true if set S contains value V as an element.

    >>> s = Link(1, Link(3, Link(2)))
    >>> contains(s, 2)
    True
    >>> contains(s, 5)
    False
    """
    if empty(s) or s.first > v:
        return False
    elif s.first == v:
        return True
    else:
        return cotains(s.rest, v)

def adjoin(s, v):
    if empty(s) or s.first > v:
        return Link(v, s)
    elif s.first == v:
        return s
    else:
        return Link(s.first, adjoin(s.rest, v))

def intersect(set1, set2):
    if  empty(set1) or empty(set2):
        return Link.empty
    else:
        e1, e2 = set1.first, set2.first
        if e1 == e2:
            return Link(e1, intersect(set1.rest, set2.rest))
        elif e1 < e2:
            return Link(set1.rest, set2)
        elif e2 < e1:
            return Link(set1, set2.rest)

def union(set1, set2):
    if empty(set1):
        return set2
    elif empty(set2):
        return set1
    else:
        e1, e2 = set1.first, set2.first
        if e1 == e2:
            return Link(e1, union(set1.rest, set2.rest))
        elif e1 < e2:
            return Link(e1, union(set1.rest, set2))
        else:
            return Link(e2, union(set1, set2.rest))

# sets mutation

def add(s, v):
    """Add v to a set s and return s."""
    assert not empty(s), 'Cannot add to an empty set.'
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and empty(s.rest):
        s.rest = Link(v)
    elif s.first < v:
        s.rest = add(s.rest, v)
    return s
