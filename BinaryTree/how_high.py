class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def how_high(root):
    stack = [root]
    right_count = 0
    left_count = 0

    if root is None:
        return -1

    while stack:
        node = stack.pop()

        if node.right:
            stack.append(node.right)
            right_count += 1
        
        if node.left:
            stack.append(node.left)
            left_count += 1
    print(right_count)
    print(left_count)
    return max(right_count, left_count)
    

print(how_high(a))