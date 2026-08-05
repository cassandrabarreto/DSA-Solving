

""" 
Write a function, linked_list_cycle, that takes in the head of a linked list as an argument. 
The function should return a boolean indicating whether or not the linked list contains a cycle.
"""
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_cycle(head):
    current = head
    values = set()

    while current is not None:
        if current.val not in values:
            values.add(current.val)
        else:
            return True
        current = current.next
    return False


def linked_list_cycle_pointers(head):
    slow = head
    fast = head
    first_iteration = True

    while not ( fast is  None and fast.next is None):
        if slow is fast and not first_iteration:
            return True
        slow = slow.next
        fast = fast.next.next
        first_iteration = False
    return False