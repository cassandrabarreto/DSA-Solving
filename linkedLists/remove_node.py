"""
Write a function, remove_node, that takes in the head of a linked list and a target value.
The function should delete the node containing the target value from the linked list
and return the head of the resulting linked list.
If the target appears multiple times in the linked list, only remove the first instance.
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


def remove_node(head, target):
    current = head
    prev = None

    if head.val == target:
        return head.next

    while current is not None:
        if current.val == target:
            prev.next = current.next
            break
        prev = current
        current = current.next
    return head
