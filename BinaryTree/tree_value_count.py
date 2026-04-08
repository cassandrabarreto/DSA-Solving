from collections import deque

def tree_value_count(root, target):

    if not root:
        return 0

    queue = deque([root])
    count = 0

    while queue:
        node = queue.popleft()

        if node.val == target:
            count += 1 

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return count


def tree_value_count(root, target):

    if not root:
        return 0

    stack = [root]
    count = 0

    while stack:
        node = stack.pop()

        if node.val == target:
            count += 1 

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return count