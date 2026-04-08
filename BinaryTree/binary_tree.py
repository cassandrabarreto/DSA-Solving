class Node:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e



def depth_first_values(root):
    # If the three is empty
    if not root:
        return []
    
    stack = [root]
    vals = []

    while stack:
        # Take element from stack
        node = stack.pop()
        # Save node in list
        vals.append(node)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return vals






