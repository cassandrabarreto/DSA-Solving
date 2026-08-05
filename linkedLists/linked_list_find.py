""" 
    Write a function, linked_list_find, that takes in the head of a linked list and a target value. 
    The function should return a boolean indicating whether or not the linked list contains the target.
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

def find(head, target):
    current = head

    while current is not None:
        if target == current.val:
            return True
        current = current.next
    return False