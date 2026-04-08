

""" 
    Write a function, tree_levels, that takes in the root of a binary tree. 
    The function should return a 2-Dimensional list where each sublist represents a level of the tree.

"""

def tree_levels(root):
    if root is None:
        return []
    
    levels = []
    stack = [(root, 0)]

    while stack:
        node , level = stack.pop()

        if len(levels) == level:
            levels.append([node.val])
        else:
            levels[level].append(node.val)

        if node.right:
            stack.append((node.right, level + 1))
        if node.left:
            stack.append((node.left, level + 1))
    return levels
    