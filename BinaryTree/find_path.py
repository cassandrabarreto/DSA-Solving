

def path_finder(root, target):

    result = _path_finder(root, target)

    if result is None:
        return None
    result = result[::-1]
    return result


def _path_finder(root, target):
    if root is None:
        return None
    
    if root.val == target:
        return [ root.val ]
    

    left_side = _path_finder(root.left, target)

    right_side = _path_finder(root.right, target)

    if left_side is not None:
        left_side.append(root.val)
        return left_side
    
    if right_side is not None:
        right_side.append(root.val)
        return right_side
    return None
    

def tree_value_count(root, target):
    if not root:
        return 0
    stack = [root]
    counter = 0

    while stack:
        node = stack.pop()

        if node.val == target:
            counter += 1

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return counter



def how_high(root):
    if root is None:
        return -1
    return max(how_high(root.left), how_high(root.right)) + 1


from collections import deque
def bottom_right_value(root):
    queue = deque([root])
    last = 0

    while queue:
        node = queue.popleft()
        last = node.val
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right) 
    return last


def all_tree_paths(root):
    paths = _all_tree_paths(root)
    for path in paths:
        path.reverse()
    return paths

def _all_tree_paths(root):
    if root is None:
        return []
    
    if root.left is None and root.right is None:
        return [[ root.val ]]
    
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
    

