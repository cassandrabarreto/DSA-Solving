"""
Write a function, linked_list_values, that takes in the head of a linked list as an argument.
The function should return a list containing all values of the nodes in the linked list

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


def linked_list_values_recursion(head):
    if head is None:
        return
    nums = []
    nums.append(head.val)
    #nums = [head.val]
    linked_list_values_recursion(head.next)


#print(linked_list_values_recursion(a))



def linked_list_values(head):
    current = head
    result = []
    while current is not None:
        result.append(current.val)
        current = current.next
    return result

print(linked_list_values(a))