
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth_first_values(root):
    if not root:
        return []
    
    values = []
    stack = [root]

    while stack:
        #take element out of stack
        node = stack.pop()
        #append it to final array
        values.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return values


def longest_streak(head):
    current = head
    max_streak = 0
    current_streak = 0
    previous_val = None

    while current is not None:
        if current.val == previous_val:
            current_streak += 1
        else:
            current_streak = 1
        if current_streak > max_streak:
            max_streak = current_streak
        previous_val = current.val
        current = current.next
    return max_streak


def is_univalue_list(head):
    current = head
    head_val = head.val

    while current is not None:
        if current.val != head_val:
            return False
        current = current.next
    return True

def merge_lists(head1, head2):
    current1 = head1
    current2 = head2
    dummy = Node(None)
    tail = dummy

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
    return dummy.next


def zipper_lists(head1, head2):
    current1 = head1.next
    current2 = head2
    counter = 0
    tail = head1

    while current1 is not None and current2 is not None:
        if counter % 2 == 0:
            # Select element from second list
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next
        counter += 1
        tail = tail.next
    if current1 is not None:
        tail.next = current1
    if current2 is not None:
        tail.next = current2
    
    return head1

def reverse_list(head):
    current = head
    prev = None
    
    while current is not None:
        # save up next
        next = current.next

        #move pointer towards prev
        current.next = prev

        # Update next
        prev = current

        # move forward
        current = next
    return prev


def depth_first_values(root):
    if not root:
        return []
    
    stack = [root]
    values = []

    while stack:
        node = stack.pop()
        values.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return values