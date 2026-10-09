
""" 
    Write a function, lowest_common_ancestor, 
    that takes in the root of a binary tree and two values. 
    The function should return the value of the lowest common ancestor of the two values in the tree.
    You may assume that the tree values are unique and the tree is non-empty.
    Note that a node may be considered an ancestor of itself.

    #      a
    #    /    \
    #   b      c
    #  / \      \
    # d   e      f
    #    / \
    #    g  h

lowest_common_ancestor(a, 'd', 'h') -> b

"""

def lowest_common_ancestor(root, val1, val2):
    path1 = find_ancestor_paths(root, val1)
    path2 = find_ancestor_paths(root, val2)

    set2 = set(path2)

    for val in path1:
        if val in set2:
            return val

def find_ancestor_paths(root, target):
    if root is None:
        return None
    # Base Cases
    if root.val == target:
        return [root.val]

    left_trace = find_ancestor_paths(root.left, target)
    if left_trace is not None:
        left_trace.append(root.val)
        return left_trace
        
    right_trace = find_ancestor_paths(root.right, target)
    if right_trace is not None:
        right_trace.append(root.val)
        return right_trace
