






from collections import deque

def tree_averages(root):
    levels = []

    if root is None:
        return []

    queue = deque([(root, 0)])

    while queue:
        node , level = queue.popleft()

        # If it does not exist, append new list.
        if len(levels) == level:
            levels.append([node.val])
        # If the level list exists, add the level's num
        else:
            levels[level].append(node.val)

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    return levels



from statistics import mean

def level_averages(root):
    level_nums= _level_averages(root)
    averages = []

    if root is None:
        return []

    for level_list in level_nums:
        avg = mean(level_list)
        averages.append(avg)
    return averages

def _level_averages(root):
    queue = deque([(root, 0)])
    levels = []

    while queue:
        current , level = queue.popleft()

        if len(levels) == level:
            levels.append([current.val])
        else:
            levels[level].append(current.val)

        if current.left:
            queue.append((current.left , level + 1))
        if current.right:
            queue.append((current.right , level + 1))
    return levels


def leaf_list(root):
    if root is None:
        return []
    leaves = []
    _leaf_list(root, leaves)
    return leaves


def _leaf_list(root, leaf_list):
    if root is None:
        return 
    if root.right is None and root.left is None:
        leaf_list.append(root.val)
    
    _leaf_list(root.left, leaf_list)
    _leaf_list(root.right, leaf_list)

