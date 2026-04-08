"""
Write a function, tree_includes, that takes in the root of a binary tree and a target value.
The function should return a boolean indicating whether or not the value is contained in the tree.
"""

from collections import deque


def tree_includes_dfs(root, target):
    if not root:
        return False

    stack = [root]

    while stack:
        node = stack.pop()

        if node.val == target:
            return True

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return False


def tree_includes_bfs(root, target):
    if not root:
        return False

    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node.val == target:
            return True

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return False
