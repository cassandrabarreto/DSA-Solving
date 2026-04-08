"""
Write a function, max_path_sum, that takes in the root of a binary tree that contains number values.
The function should return the maximum sum of any root to leaf path within the tree.
You may assume that the input tree is non-empty.
"""


def max_path_sum(root):
    if root is None:
        return float("-inf")
    if root.left is None and root.right is None:
        return root.val

    return root.val + max(max_path_sum(root.left), max_path_sum(root.right))
