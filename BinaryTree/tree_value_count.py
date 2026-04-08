"""
Write a function, tree_value_count, that takes in the root of a binary tree and a target value.
The function should return the number of times that the target occurs in the tree.
"""

from collections import deque


def tree_value_count(root, target):
    if not root:
        return 0

    queue = deque([root])
    count = 0

    while queue:
        node = queue.popleft()

        if node.val == target:
            count += 1

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return count
