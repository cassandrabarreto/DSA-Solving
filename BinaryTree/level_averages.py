

from collections import deque
def level_averages(root):
    if root is None:
        return []
    queue = deque([(root, 0)])

    while queue:
        node, level = queue.popleft()
        levels = []

        if len(levels) == level:
            levels.append([node.val])
        else:
            levels[level].append(node.val)
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1 ))
    
    return average