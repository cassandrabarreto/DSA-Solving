"""
Write a function, tree_min_value, that takes in the root of a binary tree that contains number values.
The function should return the minimum value within the tree.
"""

from collections import deque


def tree_min_value_dfs(root):
    stack = [root]
    values = []

    while stack:
        node = stack.pop()
        values.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return min(values)


def tree_min_value_bfs(root):
    queue = deque([root])
    values = []

    while queue:
        node = queue.popleft()
        values.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return min(values)
