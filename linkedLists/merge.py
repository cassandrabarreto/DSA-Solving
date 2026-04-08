"""
Write a function, merge_lists, that takes in the head of two sorted linked lists as arguments. 
The function should merge the two lists together into single sorted linked list. 
The function should return the head of the merged linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty and contain increasing sorted numbers.

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node(5)
b = Node(7)
c = Node(10)
d = Node(12)
e = Node(20)
f = Node(28)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

q = Node(6)
r = Node(8)
s = Node(9)
t = Node(25)
q.next = r
r.next = s

# 5 -> 7 -> 10 -> 12 -> 20 -> 28

def merge_lists(head1, head2):
    dummy_head = Node(None)
    current1 = head1
    current2 = head2
    tail = dummy_head

    while current1 is not None and current2 is not None:
        if current1.val < current2.val:
            tail.next = current1
            current1 = current1.next
        else:
            tail.next = current2
            current2 = current2.next
        tail = tail.next

    if current1 is not None:
        tail.next = current1
    if current2 is not None:
        tail.next = current2
    return dummy_head.next