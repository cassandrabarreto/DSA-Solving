"""
Write a function, bottom_right_value, that takes in the root of a binary tree.
The function should return the right-most value in the bottom-most level of the tree.
You may assume that the input tree is non-empty.
"""

from collections import deque


def bottom_right_value(root):
    queue = deque([root])
    last = None

    while queue:
        current = queue.popleft()
        last = current.val

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return last
