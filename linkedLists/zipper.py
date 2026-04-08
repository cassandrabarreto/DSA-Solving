""" 
Write a function, zipper_lists, that takes in the head of two linked lists as arguments. 
The function should zipper the two lists together into single linked list by alternating nodes. 
If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes.
 The function should return the head of the zippered linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty.
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


x = Node('X')
y = Node('Y')
z = Node('Z')

x.next = y
y.next = z


def zipper_lists(head1, head2):
    # Tail always starts as List 1 head
    tail = head1
    current1 = head1.next
    current2 = head2
    count = 0

    while current1 is not None and current2 is not None:
        if count % 2 == 0:
            # Make next element from list 2 
            tail.next = current2
            # Shift pointer 
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next

        #make next one the tail
        tail = tail.next
        count += 1

    if current1 is not None:
        tail.next = current1
    if current2 is not None:
        tail.next = current2
    return head1


zipper_lists(a, x)