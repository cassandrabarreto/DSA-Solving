"""
Write a function, how_high, that takes in the root of a binary tree.
The function should return a number representing the height of the tree.
The height of a binary tree is defined as the maximal number of edges from the root node to any leaf node.
If the tree is empty, return -1.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


def how_high(root):
    if root is None:
        return -1
    return 1 + max(how_high(root.left), how_high(root.right))


print(how_high(a))
