""" 
Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. 
The function should return the total sum of all values in the linked list.

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node(3)
b = Node(2)
c = Node(1)

a.next = b
b.next = c


def sum_list(head):
    current = head
    sum = 0

    while current is not None:
        sum += current.val
        current = current.next
    return sum

print(sum_list(a))