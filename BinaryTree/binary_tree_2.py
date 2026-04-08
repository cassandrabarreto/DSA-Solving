



def depth_first_values(root):
    stack = [root]
    values = []

    if not root:
        return []

    while stack:
        node = stack.pop()
        values.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return values

from collections import deque

def breadth_first_values(root):
    if not root:
        return []

    queue = deque([root])
    values = []

    while queue:
        node = queue.popleft()
        values.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return values


def max_path_sum(root):
    if root is None:
        return float("-inf")
    if root.left is None and root.right is None:
        return root.val
    
    return root.val + max(max_path_sum(root.left), max(root.right))


def path_finder(root, target):
    paths_lst = _path_finder(root,target)
    if root is None:
        return None
    
    paths_lst = paths_lst[::-1]
    return paths_lst


def _path_finder(root, target):
    if root is None:
        return None
    
    if root.val == target:
        return [root.val]

    left = _path_finder(root.left, target)
    if left is not None:
        left.append(root.val)
        return left
    right = _path_finder(root.right, target)
    if right is not None:
        right.append(root.val)
        return right
    return None















def max_path_sum(root):
    if root is None:
        return float("-inf")
    if root.right is None and root.left is None:
        return root.val
    
    return root.val + max(max_path_sum(root.left), max_path_sum(root.right))





""" 
    
Write a function, path_finder, that takes in the root of a binary tree and a target value.
The function should return an array representing a path to the target value. 
If the target value is not found in the tree, then return None.

"""
def path_finder(root, target):
    if root is None:
        return None
    
    if root.val == target:
        return [root.val]
    


def max_path_sum(root):
    if root is None:
        return float('-inf')
    if root.right is None and root.left is None:
        return root.val
    
    return root.val + max(max_path_sum(root.left), max_path_sum(root.right))










def path_finder(root, target):
    result = _path_finder(root, target)
    if result is None:
        return None
    else:
        return result[::-1]

def _path_finder(root, target):
    if root is None:
        return None
    
    if root.val == target:
        return [root.val]
    
    left_path = _path_finder(root.left, target)
    right_path = _path_finder(root.right, target)

    if left_path is not None:
        left_path.append(root.val)
        return left_path
    
    if right_path is not None:
        right_path.append(root.val)
        return left_path
    return None