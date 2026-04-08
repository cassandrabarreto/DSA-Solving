"""
Write a function, insert_node, that takes in the head of a linked list, a value, and an index.
The function should insert a new node with the given value into the list at the specified index.
Consider the head of the linked list as index 0.
The function should return the head of the resulting linked list.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def insert_node(head, value, index):
    current = head
    i = 0

    if index == 0:
        new_head = Node(value)
        new_head.next = head
        return new_head
    
    while current is not None:
        if i == (index - 1):
            temp = current.next
            new_node = Node(value)
            current.next = new_node
            current.next.next = temp
        i += 1
        current = current.next
    return head
