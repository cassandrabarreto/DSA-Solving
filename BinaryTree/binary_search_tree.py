

""" 
    Write a function, binary_search_tree_includes, 
    that takes in the root of a binary search tree containing numbers and a 
    target value. The function should return a boolean indicating whether or not the target is found within the tree.
    A Binary Search Tree is a binary tree where all values within a node's left subtree are smaller than the node's value and all values in a node's 
    right subtree are greater than or equal to the node's value.
    Your solution should have a best case runtime of O(log(n)).
"""
def binary_search_tree_includes(root, target):
    if root is None:
        return False
    if root.val == target:
        return True
    if target < root.val:
        return binary_search_tree_includes(root.left, target)
        
    else:
        return binary_search_tree_includes(root.right, target)





















""" 
Write a function, level_averages, that takes in the root of a binary tree that contains number values. 
The function should return a list containing the average value of each level.    
"""

from statistics import mean
from collections import deque
def level_averages(root):
    if root is None:
        return []

    averages = []

    level_nums = get_level_nums(root)

    for level in level_nums:
        average = mean(level)
        averages.append(average)
    return averages
    

def get_level_nums(root):
    
    level = 0
    level_numbers = []
    queue = deque([(root, level)])

    while queue:
        current , level = queue.popleft()

        if len (level_numbers) > level:
            level_numbers[level].append(current.val)
        else:
            level_numbers.append([current.val])
            
        # level logic
        if current.left is not None:
            queue.append((current.left, level + 1 ))

        if current.right is not None:
            queue.append((current.right, level + 1 ))
    
    return level_numbers