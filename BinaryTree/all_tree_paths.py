

def all_tree_paths(root):
    all_paths = _all_tree_paths(root)
    for path in all_paths:
        path.reverse()
    return all_paths

def _all_tree_paths(root):
    if root is None:
        return []
    
    if root.left is None and root.right is None:
        return [[root.val]]
    
    all_paths = []

    right_paths = _all_tree_paths(root.right)

    for path in right_paths:
        path.append(root.val)
        all_paths.append(path)

    left_paths = _all_tree_paths(root.left)

    for path in left_paths:
        path.append(root.val)
        all_paths.append(path)

    return all_paths


from collections import deque

def bottom_right_value(root):
    
    queue = deque([root])
    last_val = 0

    while queue:
        node = queue.popleft()
        last = node.val

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return last
    
def how_high(root):
    if root is None:
        return -1
    
    return max(how_high(root.right), how_high(root.left)) +1




def path_finder(root,target):
    result = path_finder(root,target)
    if result is None:
        return None
    else:
        return result[::-1]

def _path_finder(root, target):
    if root is None:
        return None
    if target == root.val:
        return[root.val]
    
    right_side = _path_finder(root.right, target)
    if right_side is not None:
        right_side.append(root.val)
        return right_side
    
    left_side = _path_finder(root.left, target)
    if left_side is not None:
        left_side.append(root.val)
        return left_side

    return None