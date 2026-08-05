

""" 
Write a function, middle_value, that takes in the head of a
linked list as an argument. The function should return the value 
of the middle node in the linked list. If the linked list has an even number 
of nodes, then return the value of the second middle node.
You may assume that the input list is non-empty.
"""
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    
def middle_value(head):
    current = head
    values = []
    # Phase 1: Traverse through list
    while current is not None:
        values.append(current.val)
        current = current.next
    # Phase 2: Calculate middle point. Floor in case lenght of list is not even.
    i = len(values) // 2
    return values[i]