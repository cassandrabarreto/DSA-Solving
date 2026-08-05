""" 
Write a function, linked_palindrome, that takes in the head of a linked list as an argument.
The function should return a boolean indicating whether or not the linked list is a palindrome. 
A palindrome is a sequence that is the same both forwards and backwards.
"""

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_palindrome(head):
    current = head
    list_seq = []

    while current is not None:
        list_seq.append(current.val)
        current = current.next
    
    return list_seq == list_seq[::-1]