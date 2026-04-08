"""
Write a function, path_finder, that takes in the root of a binary tree and a target value.
The function should return an array representing a path to the target value.
If the target value is not found in the tree, then return None.
You may assume that the tree contains unique values.
"""


def path_finder(root, target):
    if root is None:
        return None

    result = _path_finder(root, target)

    if result is None:
        return None
    return result[::-1]


def _path_finder(root, target):
    if root is None:
        return None

    if root.val == target:
        return [root.val]

    left_path = _path_finder(root.left, target)
    if left_path is not None:
        left_path.append(root.val)
        return left_path

    right_path = _path_finder(root.right, target)
    if right_path is not None:
        right_path.append(root.val)
        return right_path

    return None
