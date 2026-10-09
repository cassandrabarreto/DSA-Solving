""" 
    Write a function, post_order, that takes in the root of a binary tree. 
    The function should return a list containing the post-ordered values of the tree.
    Post-order traversal is when nodes are recursively visited in the order: left child, right child, self.    
"""

def post_order(root):
    if root is None:
        return []
    
    final_result = []
    post_order_traversal(root, final_result)
    return final_result

def post_order_traversal(root, ordered_list):
    if root is None:
        return None
    post_order_traversal(root.left, ordered_list)
    post_order_traversal(root.right, ordered_list)
    ordered_list.append(root.val)
    