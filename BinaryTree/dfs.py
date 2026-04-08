

def tree_sum_dfs(root):
    result = 0
    stack = [root]

    if not root:
        return 0
    
    while stack:
        node = stack.pop()
        result += node.val

        if node.right:
            stack.append(node.right)
        
        if node.left:
            stack.append(node.left)
    return result


from collections import deque

def tree_sum_bfs(root):
    result = 0
    queue = deque([root])

    if not root:
        return 0
    
    while queue:
        node = queue.popleft()
        result += node.val

        if node.left:
            queue.append(node.left)
        
        if node.right:
            queue.append(node.right)
    return result


""" Write a function, tree_includes, that takes in the root of a binary tree and a target value. 
The function should return a 
boolean indicating whether or not the value is contained in the tree."""

def tree_includes_dfs(root, target):
    if not root:
        return False

    stack = [root]

    while stack:
        node = stack.pop()
        
        if node.val == target:
            return True
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return False
        

def tree_includes_bfs(root, target):
    if not root:
        return False

    queue = deque([root])

    while queue:

        node = queue.popleft()
        
        if node.val == target:
            return True
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return False
    

"""
Write a function, tree_min_value, that takes in the root of a binary tree that contains number values. 
The function should return the minimum value within the tree.
"""

def tree_min_value(root):
    stack = [root]
    values = []

    while stack:
        node = stack.pop()
        values.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return min(values)


def tree_min_value(root):
    queue = deque([root])
    values = []

    while queue:
        node = queue.popleft()
        values.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return min(values)


"""
Write a function, max_path_sum, that takes in the root of a binary tree that contains number values.
The function should return the maximum sum of any root to leaf path within the tree.

You may assume that the input tree is non-empty.

"""

def max_path_sum(root):
    stack = [root]
    result = 0

    while stack:
        node = stack.pop()

        if node.right():
            stack.append(node.right)
            path1 = node.val + node.right.val
        if node.left():
            path2 = node.val + node.left.val
            stack.append(node.left)

    print(path1)
    print(path2)
    return path1 + path2

