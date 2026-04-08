"""
Write a function, tree_sum, that takes in the root of a binary tree that contains number values.
The function should return the total sum of all values in the tree.
"""

from collections import deque


def tree_sum_dfs(root):
    if not root:
        return 0

    result = 0
    stack = [root]

    while stack:
        node = stack.pop()
        result += node.val

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


def tree_sum_bfs(root):
    if not root:
        return 0

    result = 0
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result += node.val

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
