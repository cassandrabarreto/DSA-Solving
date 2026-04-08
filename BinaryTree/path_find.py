
#path_finder(a, 'e') # -> [ 'a', 'b', 'e' ]


def path_finder(root,target):
    result = _path_finder(root,target)
    if result is None:
        return None
    else:
        return result[::-1]


def _path_finder(root, target):
    if root is None:
        return None
    if root.val == target:
        return [root.val]

    left_side = _path_finder(root.left, target)
    if left_side is not None:
        left_side.append(root.val)
        return left_side

    right_side = _path_finder(root.right, target)
    if right_side is not None:
        right_side.append(root.val)
        return right_side
    return None




from collections import deque
def tree_levels(root):
    if root is None:
        return []
    queue = deque([(root,0)])
    levels = []

    while queue:
        current , level = queue.popleft()

        if len(levels) == level:
            levels.append([current.val])
        else:
            levels[level].append(current.val)

        if current.left is not None:
            queue.append((current.left, level + 1))

        if current.right is not None:
            # Increment Level
            queue.append((current.right, level + 1))
        
    return levels


from statistics import mean
from collections import deque

def level_averages(root):
    if root is None:
        return None
    
    levels = _level_averages(root)
    averages = []

    for level in levels:
        average = mean(level)
        averages.append(average)
    return averages
    

def _level_averages(root):
    if root is None:
        return None
    
    queue = deque([(root,0)])
    levels = []

    while queue:
        current , level_number = queue.popleft()

        if len(levels) == level_number:
            levels.append([current.val])
        else:
            levels[level_number].append(current.val)

        if current.left is not None:
            queue.append((current.left, level_number + 1))
        if current.right is not None:
                queue.append((current.right, level_number + 1))
    return levels


def how_high(root):
    if root is None:
        return -1
    if root.right is None and root.left is None:
        return 0
    return 1 + max(how_high(root.right), how_high(root.left))




def leaf_list(root):
    if root is None:
        return []
    nodes_list = []
    _leaf_list(root, nodes_list)
    return nodes_list

def _leaf_list(root, lst):
    if root is None:
        return
    if root.left is None and root.right is None:
        lst.append(root.val)
        
    _leaf_list(root.left, lst)
    _leaf_list(root.right, lst)
