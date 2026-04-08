""" 
    Write a function, max_path_sum, that takes in the root of a binary tree that contains number values. 
    The function should return the maximum sum of any root to leaf path within the tree.

"""


def max_path_sum(root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        return root.val
    
    return root.val + max(max_path_sum(root.left), max_path_sum(root.right))