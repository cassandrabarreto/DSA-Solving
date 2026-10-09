""" 
    Write a function, flip_tree, that takes in the root of a binary tree. 
    The function should flip the binary tree, turning left subtrees into 
    right subtrees and vice-versa. This flipping should occur in-place by 
    modifying the original tree. The function should return the root of the tree.
"""


def flip_tree(root):
    # Base Case to handle none nodes
    if root is None:
        return None

    left = flip_tree(root)
    right = flip_tree(root)

    root.left = right
    root.right = left

    return root

