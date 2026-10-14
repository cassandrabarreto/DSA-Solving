""" 
    Write a function, is_tree_balanced, that takes in the root of a binary tree. 
    The function should return a boolean indicating whether or not the tree is "balanced".
    A "balanced" binary tree is a binary tree where the height between the left and right subtrees 
    differs by at most 1 for every node.    
"""

class Node():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        
def is_tree_balanced(root):
    return check_tree_balance(root) > -1

def check_tree_balance(root):
    if root is None:
        return 0
    
    left_height = check_tree_balance(root.left)
    right_height =  check_tree_balance(root.right)

    if left_height == -1:
        return -1
    if right_height == -1:
        return -1

    # If this subtraction is more than 1, that means that the tree is unbalanced.
    if abs(left_height - right_height) > 1:
        return -1
    else:
        return 1 + max(left_height, right_height)
    


root = Node('*')
root.left = Node('+')
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(4)


def build_unbalanced_tree():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    a.left = b
    b.left = c
    c.left = d
    a.right = e

    return a 

def build_balanced_tree():
    m = Node('m')
    n = Node('n')
    o = Node('o')
    x = Node('x')
    y = Node('y')

    m.left = n
    m.right = o
    n.left = x
    n.right = y

    return m


def run_tests():
    a = build_unbalanced_tree()
    assert not is_tree_balanced(a) , "Test Failed: Unbalanced tree is expected"

    x = build_balanced_tree()
    assert is_tree_balanced(x) , "Test Failed: Balanced tree is expected"



