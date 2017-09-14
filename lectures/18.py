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
