"""
Write a function, tree_levels, that takes in the root of a binary tree.
The function should return a 2-Dimensional list where each sublist represents a level of the tree.
"""

from collections import deque


def tree_levels(root):
    if root is None:
        return []

    levels = []
    queue = deque([(root, 0)])

    while queue:
        node, level = queue.popleft()

        if len(levels) == level:
            levels.append([node.val])
        else:
            levels[level].append(node.val)

        if node.left is not None:
            queue.append((node.left, level + 1))
        if node.right is not None:
            queue.append((node.right, level + 1))
    return levels
