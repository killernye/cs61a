class Tree:
    def __init__(self, root, branches=[]):
        self.root = root
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.root, branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self, k=0):
        indented = []
        for b in self.branches:
            for line in b.indented(k + 1):
                indented.append(' ' + line)
        return [str(self.root)] + indented

    def is_leaf(self):
        return not self.branches

def memo(f):
    cache = {}
    def memorized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memorized

@memo
def fib_tree(n):
    if n == 0 or n == 1:
        return BTree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.root + right.root
        return BTree(fib_n, left, right)

def leaves(t):
    if t.is_leaf():
        return [t.root]
    else:
        return sum([leaves(b) for b in t.branches],[])

def prune_repeats(t, seen):
    t.branches = [b for b in t.branches if b not in seen]
    seen.append(t)
    for b in t.branches:
        prue_repeats(b, seen)

def hailstone(n):
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return hailstone(n//2) + 1
    else:
        return hailstone(3*n + 1) + 1

def is_int(x):
    return int(x) == x

def is_odd(x):
    return x % 2 == 1

def hailstone_tree(k, n=1):
    """Return a Tree in which the paths from the leaves to the root are all possible hailstone sequences of length k ending in n."""
    if k == 1:
        return Tree(n)
    else:
        greater, less = 2*n, (n-1)/2
        branches = []
        branches.append(hailstone_tree(k-1, greater))
        if less > 1 and is_int(less) and is_odd(less):
            branches.append(hailstone_tree(k-1), int(less))
        return Tree(n, branches)

def longest_path_below(k, t):
    if t.root > k:
        return []
    elif t.is_leaf():
        return [t.root]
    else:
        paths=[longest_path_below(k, b) for b in t.branches]
        return [t.root] + max(paths, key=len)

# Binary Tree class

class BTree(Tree):
    empty = Tree(None)

    def __init__(self, root, left=empty, right=empty):
        for b in (left, right):
            assert isinstance(b, BTree) or b is BTree.empty
        Tree.__init__(self, root, [left, right])

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]

    def is_leaf(self):
        return [self.left, self.right] == [BTree.empty] * 2

    def __repr__(self):
        if self.is_leaf():
            return 'BTree({0})'.format(self.root)
        elif self.right is BTree.empty:
            left = repr(self.left)
            return 'BTree({0},{1})'.format(self.root, left)
        else:
            left, right = repr(self.left), repr(self.right)
            if self.left is BTree.empty:
                left = 'BTree.empty'
            template = 'BTree({0}, {1}, {2})'
            return template.format(self.root, left, right)


def contents(t):
    if t is BTree.empty:
        return []
    else:
        return contents(t.left) + [t.root] + contents(t.right)

def bst(s):
    """Construct a binary search tree from a sorted list."""

    >>> bst([1, 2, 3])
    BTree(2, BTree(1), BTree(3))

    if not s:
        return BTree.empty
    else:
        mid = len(s)//2
        left, right = bst(s[:mid]), bst(s[mid+1:])
        return BTree(s[mid], left, right)

def largest(t):
    if t.right is BTree.empty:
        return t.root
    else:
        return largest(t.right)

def second(t):
    if t.is_leaf():
        return None
    elif t.right.is_leaf():
        return t.root
    elif t.right is BTree.empty:
        return largest(t.left)
    else:
        return second(t.right)

def contains(s, v):
    if s in BTree.empty:
        return False
    elif s.root == v:
        return True
    elif s.root < v:
        return contains(s.right, v)
    elif s.root > v:
        return contains(s.left, v)

def adjoin(s, v):
    if s is BTree.empty:
        return BTree(v)
    elif s.root == v:
        return s
    elif s.root < v:
        return BTree(s.root, s.left, adjoin(s.right, v))
    else:
        return BTree(s.root, adjoin(s.left, v), s.right)
