


def all_tree_paths(root):
    all_paths = _all_tree_paths(root)

    for path in all_paths:
        path.reverse()
    return all_paths


def _all_tree_paths(root):
    if root is None:
        return []
    if root.right is None and root.left is None:
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


def how_high(root):
    if root is None:
        return -1
    
    return max(how_high(root.right), how_high(root.left)) + 1



class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


def tree_levels(root):
    levels = []

    if root is None:
        return []
    
    stack = [(root,0)]

    while stack:
        node, level_num = stack.pop()

        if len(levels) == level_num:
            levels.append([node.val])
        else:
            levels[level_num].append(node.val)

        if node.right is not None:
            stack.append((node.right, level_num + 1))
        if node.left is not None:
            stack.append((node.left, level_num + 1))

    return levels
    
from collections import deque


def tree_levels(root):
    levels = []

    if root is None:
        return []
    
    queue = deque([(root,0)])

    while queue:
        node, level_num = queue.popleft()

        if len(levels) == level_num:
            levels.append([node.val])
        else:
            levels[level_num].append(node.val)
        
        if node.left is not None:
            queue.append((node.left, level_num + 1))

        if node.right is not None:
            queue.append((node.right, level_num + 1))

    return levels
