
""" 

Write a function that takes in a linked list that contains values in increasing order. 
The function should return a new linked list containing the original values, with duplicates removed. 
The relative order of values in the resulting linked list should be unchanged
You must create and return a new set of linked list nodes and not just modify the input nodes.

"""
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    
def undupe_sorted_linked_list(head):
    current = head
    dummy = Node(None)
    tail = dummy
    while current is not None:
        # Compare current to tail. Only add node if they are different
        if current.val != tail.val:
            tail.next = Node(current.val)
            tail = tail.next
        current = current.next
    return dummy.next
