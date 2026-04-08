"""
Write a function, leaf_list, that takes in the root of a binary tree
and returns a list containing the values of all leaf nodes in left-to-right order.
"""


def leaf_list(root):
    if root is None:
        return []

    leaves = []
    _leaf_list(root, leaves)
    return leaves


def _leaf_list(root, leaves):
    if root is None:
        return

    if root.left is None and root.right is None:
        leaves.append(root.val)

    _leaf_list(root.left, leaves)
    _leaf_list(root.right, leaves)
