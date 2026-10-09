""" 
    
Write a function, is_binary_search_tree, that takes in the root of a binary tree. 
The function should return a boolean indicating whether or not the tree satisfies the binary 
search tree property.

A Binary Search Tree is a binary tree where all values within a node's left subtree are 
smaller than the node's value and all values in a node's right subtree are greater than the node's value.

"""

def is_binary_search_tree(root):
    numbers = []
    in_order_traversal(root, numbers)

    if is_sorted(numbers):
        return True
    return False

def in_order_traversal(root, numbers):
    if root is None:
        return None
    in_order_traversal(root.left, numbers)
    numbers.append(root.val)
    in_order_traversal(root.right, numbers)

def is_sorted(numbers):
    for idx in range(0, len(numbers)-1):
        # check element
        current = numbers[idx]
        nxt = numbers[idx + 1 ]
        if nxt < current:
            return False
    return True