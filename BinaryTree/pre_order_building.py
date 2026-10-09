class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree_in_pre(in_order, pre_order):
    if len(in_order) == 0:
        return None

    # in pre order the first val is the root
    root_val = pre_order[0]
    root = Node(root_val)

    #calculate mid element
    mid = in_order.index(root_val)

    # obtain left side of in order
    left_in_order = in_order[:mid]

    # obtain right side of in order
    right_in_order = in_order[mid + 1:]

    left_size = len(left_in_order)

    left_pre_order = pre_order[1: 1 + left_size]

    right_pre_order = pre_order[1 + left_size:]

    root.left = build_tree_in_pre(left_in_order, left_pre_order)
    root.right = build_tree_in_pre(right_in_order, right_pre_order)

    return root