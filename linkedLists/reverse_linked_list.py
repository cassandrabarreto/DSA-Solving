"""
Write a function, reverse_list, that takes in the head of a linked list as an argument.
 The function should reverse the order of the nodes in the 
linked list in-place and return the new head of the reversed linked list.

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

def reverse_list(head):
    current = head
    prev = None
    while current is not None:
        # Save next
        next = current.next
        # Flip pointer or arrow to previous (This breaks original connection)
        current.next = prev
        # Make current Previous
        prev = current
        # Move forward to next node
        current = next
    return prev
    


reverse_list(a)
