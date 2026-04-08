"""
Write a function, all_tree_paths, that takes in the root of a binary tree.
The function should return a 2-Dimensional list where each subarray represents a root-to-leaf path in the tree.
The order within an individual path must start at the root and end at the leaf,
but the relative order among paths in the outer list does not matter.
You may assume that the input tree is non-empty.
"""


def all_tree_paths(root):
    paths = _all_tree_paths(root)

    for path in paths:
        path.reverse()
    return paths


def _all_tree_paths(root):
    if root is None:
        return []

    if root.left is None and root.right is None:
        return [[root.val]]

    all_paths = []

    left_paths = _all_tree_paths(root.left)
    for path in left_paths:
        path.append(root.val)
        all_paths.append(path)

    right_paths = _all_tree_paths(root.right)
    for path in right_paths:
        path.append(root.val)
        all_paths.append(path)

    return all_paths
