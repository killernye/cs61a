def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches is invalid data'
    return [root] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(root(left) + root(right), [left, right])

def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        count_branches = [count_leaves(branch) for branch in branches(t)]
        return sum(count_branches )

def leaves(tree):
    """Return a list containing the leaves of tree.

    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    """
    if is_leaf(tree):
        return tree
    else:
        return sum([leaves(b) for b in branches(tree)], [])

def increment_leaves(t):
    """Return a tree like t but with leaf values incremented."""
    if is_leaf(t):
        return tree(root(t) + 1)
    else:
        return tree(root(t), [increment_leaves(b) for b in branches(t)])

def increment(t):
    """Return a tree like t but with all node values incremented."""
    return tree(root(t)+1, [increment(b) for b in branches(t)])

def print_tree(t, indent = 0):
    print(' ' * indent + str(root(t)))
    for b in branches(t):
        print_tree(b, indent+1)

def height(t):
    """Return the height of a tree"""
    if is_leaf(t):
        return 0
    else:
        return 1 + max([height(b) for b in branches(t)])

def tree_max(t):
    """Return the max of a tree."""
    if is_leaf(t):
        return root(t)
    else:
        largest_in_branches = max([tree_max(b) for b in branches(t)])
        return max(root(t), largest_in_branches)

def find_path(tree, x):
    """Returns a list containing the nodes along the path to get from the root of tree
    to a node x. if x is not present in tree, return None""
    >>> t = tree(2, [[7, [3], [6, [5], [11]]], [15]])
    [2, 7, 6, 5]
    >>> find_path(t, 10) # return None
    """
    if root(tree) == x:
        return [x]
    else:
        for path in [find_path(b, x) for b in branches(tree)]:
            if path:
                return [root(tree)] + path

def prune(t, k):
    """Return a new tree that is a copy of only the first K
    levels of tree T."""
    if k == 0:
        return [root(t)]
    else:
        return tree(root(t),[prune(b, k - 1) for b in branches(t)])

def delete(t, r_b):
    """Deletes a branch with root value of R_B. You will not delete the T itself.
    Return the new tree.

    kept_branches = []
    for b in branches(t):
        if root(b) == r_b:
            kept_branches += []
        else:
            kept_branches += delete(b, r_b)
    return tree(root(t), kept_branches)
    """
    return tree(root(t), [delete(b, r_b) for b in branches(t) if root(b) != r_b])

def add_leaf(t, r_b, leaf):
    """Add a leaf to the branch B of the tree T.And return the new tree."""
    if root(t) == r_b:
        return tree(root(t), branches(t) + [tree(leaf)])
    else:
        return tree(root(t), [add_leaf(b, r_b, leaf) for b in branches(t)])


def find_path_list(t, x):
    if root(t) == x:
        return [[root(t)]]
    else:
        res = []
        for path_list in [find_path_list(b, x) for b in branches(t)]:
            if path_list:
                res += path_list
        if res == []:
            return None
        return [[root(t)] + p for p in res]
