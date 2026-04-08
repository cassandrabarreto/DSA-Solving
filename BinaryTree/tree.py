
def path_finder(root,target):
    if root is None:
        return None
    
    path = _path_finder(root, target)

    if path is None:
        return None
    else:
        return path[::-1]
        


def _path_finder(root, target):
    if root is None:
        return None
    # Base Case
    if root.val == target:
        return [root.val]
    

        # Recursion Step
    left_path = _path_finder(root.left, target)
    if left_path is not None:
        left_path.append(root.val)
        return left_path
    

    right_path = _path_finder(root.right, target)
    if right_path is not None:
        right_path.append(root.val)
        return right_path
    




def how_high(root):
    if root is None:
        return -1
    
    return 1 + max(how_high(root.left), how_high(root.right))



from collections import deque

def bottom_right_value(root):
    queue = deque([root])

    while queue:
        root = queue.popleft()
    

        if root.left is not None:
            queue.append(root.left)
        if root.right is not None:
                queue.append(root.right)
        
    return root.val

from collections import deque 
def breadth_first_values(root):
    values = []
    queue = deque([root])

    if root is None:
        return []
    
    while queue:
        current = queue.popleft()
        values.append(current.val)

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return values
        



def depth_first_values(root):
    stack = [root]
    values = []
    if root is None:
        return []

    while stack:
        current = stack.pop()
        values.append(current.val)

        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
    return values


"""
Write a function, max_path_sum, that takes in the root of a binary tree that contains number values. 
The function should return the maximum sum of any root to leaf path within the tree.
You may assume that the input tree is non-empty.
"""

def max_path_sum(root):
    # base case
    if root is None:
        return float('-inf')
    if root.left is None and root.right is None:
        return root.val
    
    return root.val + max(max_path_sum(root.right), max_path_sum(root.left))



""" 
    
Write a function, path_finder, that takes in the root of a binary tree and a target value. 
The function should return an array representing a path to the target value.
 If the target value is not found in the tree, then return None.
You may assume that the tree contains unique values.
"""
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

#path_finder(a, 'e') # -> [ 'a', 'b', 'e' ]


def path_finder(root, target):
    # If root is none there is no point in even getting recursive function
    if root is None:
        return None
    
    path = _path_finder(root, target)

    if path is None:
        return None
    else:
        return path[::-1]


def _path_finder(root, target):
    # Base Cases
    if root is None:
        return None
    if root.val == target:
        return [root.val]

    # Rescursive Step
    right_path = _path_finder(root.right, target)
    if right_path is not None:
        right_path.append(root.val)
        return right_path
        
    # Rescursive Step
    left_path = _path_finder(root.left, target)
    if left_path is not None:
        left_path.append(root.val)
        return left_path
    return None



""" 
    
Write a function, tree_value_count, that takes in the root of a binary tree and a target value. 
The function should return the number of times that the target occurs in the tree.
"""
from collections import deque
def tree_value_count(root, target):

    if root is None:
        return 0

    queue = deque([root])
    counter = 0

    while queue:
        current = queue.popleft()

        if current.val == target:
            counter += 1 

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return counter




""" 
Write a function, how_high, that takes in the root of a binary tree. 
The function should return a number representing the height of the tree.
The height of a binary tree is defined as the maximal number of edges from the root node to any leaf node.
If the tree is empty, return -1.
"""

def how_high(root):
    if root is None:
        return -1
    return 1 + max(how_high(root.right), how_high(root.left))



""""
Write a function, bottom_right_value, that takes in the root of a binary tree.
 The function should return the right-most value in the bottom-most level of the tree.
You may assume that the input tree is non-empty
"""
from collections import deque
def bottom_right_value(root):
    queue = deque([root])
    last = None

    while queue:
        current = queue.popleft()
        last = current.val

        if current.left is not None:
            queue.append(current.left)
            
        if current.right is not None:
            queue.append(current.right)
    return last


"""
Write a function, all_tree_paths, that takes in the root of a binary tree.
 The function should return a 2-Dimensional list where each subarray represents a root-to-leaf path in the tree.

The order within an individual path must start at the root and end at the leaf, 
but the relative order among paths in the outer list does not matter.

You may assume that the input tree is non-empty.
"""
def all_tree_paths(root):
    paths = _all_tree_paths(root)

    for path in paths:
        path = path[::-1]
    return path


def _all_tree_paths(root):
    if root is None:
        return []    
    # Base Case. when i find a leaf return a list with it
    if root.right is None and root.left is None:
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






""" 
    
Write a function, all_tree_paths, that takes in the root of a binary tree. 
The function should return a 2-Dimensional list where each subarray represents a root-to-leaf path in the tree.
The order within an individual path must start at the root and end at the leaf, but the relative order among 
paths in the outer list does not matter.
You may assume that the input tree is non-empty.

"""

def all_tree_paths(root):
    paths = _all_tree_paths(root)

    for path in paths: 
        path.reverse()
    return paths

def _all_tree_paths(root):
    if root is None:
        return []
    if root.left is None and root.right is None:
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







""" 
Write a function, tree_levels, that takes in the root of a binary tree.
The function should return a 2-Dimensional list where each sublist represents a level of the tree.
"""
from collections import deque
def tree_levels(root):
    if root is None:
        return []
    
    # Attach root and level 0 to queue
    queue = deque([(root,0)])
    levels = []

    while queue:
        # Pop element and level
        current, level = queue.popleft()

        # Check if level does not exist
        if len(levels) == level:
            levels.append([current.val])
        else:
            # If it exists just attach value to it in the levels index
            levels[level].append(current.val)
        
        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)
    return levels






from collections import deque
from statistics import mean

def level_averages(root):
    if root is None:
        return []
    
    averages = []
    levels = _level_averages(root)

    for level in levels:
        avg = mean(level)
        averages.append(avg)
    return averages


def _level_averages(root):
    
    queue = deque([(root, 0)])
    levels = []

    while queue:
        current, level = queue.popleft()

        if len(levels) == level:
            levels.append([current.val])
        else:
            levels[level].append(current.val)
        # Left and Right
        if current.left is not None:
            queue.append((current.left, level + 1 ))
        if current.right is not None:
            queue.append((current.right, level + 1 ))
    return levels




"""
Write a function, leaf_list, that takes in the root of a binary tree and returns a list containing 
the values of all leaf nodes in left-to-right order.

"""

def leaf_list(root):
    if root is None:
        return []
    
    leaves = []
    stack = [root]

    while stack:
        current = stack.pop()

        if current.right is None and current.left is None:
            leaves.append(current.val)

        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
    return leaves




def leaf_list(root):
    if root is None:
        return []
    
    leaves = []
    _leaf_list(root, leaves)
    return leaves


def _leaf_list(root, leaves):
    if root is None:
        return None
    if root.right is None and root.left is None:
        return root.val
    
    left = _leaf_list(root.left, leaves)
    if left is not None:
        leaves.append(root.val)

    right = _leaf_list(root.right, leaves)
    if right is not None:
        leaves.append(root.val)
