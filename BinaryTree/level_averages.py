"""
Write a function, level_averages, that takes in the root of a binary tree that contains number values.
The function should return a list containing the average value of each level.
"""

from collections import deque
from statistics import mean


def level_averages(root):
    if root is None:
        return []

    levels = _level_averages(root)
    averages = []

    for level in levels:
        averages.append(mean(level))
    return averages


def _level_averages(root):
    queue = deque([(root, 0)])
    levels = []

    while queue:
        current, level = queue.popleft()

        if len(levels) == level:
            levels.append([current.val])
        else:
            levels[level].append(current.val)

        if current.left is not None:
            queue.append((current.left, level + 1))
        if current.right is not None:
            queue.append((current.right, level + 1))
    return levels
