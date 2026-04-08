"""
Write a function, longest_streak, that takes in the head of a linked list as an argument. 
The function should return the length of the longest 
consecutive streak of the same value within the list.

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node(5)
b = Node(5)
c = Node(3)
d = Node(3)
e = Node(3)

a.next = b
b.next = c
c.next = d
d.next = e


def longest_streak(head):
    current = head
    prev = None
    max_streak = 0
    current_streak = 0

    while current is not None:
    
        if current.val == prev:
            current_streak += 1
        else:
            current_streak = 1
        
        prev = current.val
        if current_streak > max_streak:
            max_streak = current_streak
    
        current = current.next
    return max_streak
    

print(longest_streak(a))