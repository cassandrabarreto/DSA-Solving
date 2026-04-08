""" 
Write a function, get_node_value, that takes in the head of a linked list and an index. 
The function should return the value of the linked list at the specified index.

If there is no node at the given index, then return None.
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

def get_node_value(head, index):
    counter = 0 
    current = head

    while current is not None:
        counter += 1
        if counter == index:
            return index
        current = current.next
    return None
    