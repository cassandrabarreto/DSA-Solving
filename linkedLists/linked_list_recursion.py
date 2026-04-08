"""
Write a function that takes in the head of a linked list and prints the value of each node
by traversing the list recursively.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node('A')
b = Node('B')
c = Node('C')

a.next = b
b.next = c


def print_nodes(head):
    if head is None:
        return
    print(head.val)
    print_nodes(head.next)

print_nodes(a)