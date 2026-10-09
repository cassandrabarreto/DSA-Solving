""" 
    You are given a network of computers connected by cables. 
    A cable connects two computers and can transmit data in both directions.

    A fully-connected network is a network where all computers can communicate with each other by transmitting data through cables. 
    For example:

    1. the following network is fully-connected:
        3
        |
    0---1---2---4


    2. the following network is not fully-connected:
        3
        |
    0---1     2---4

    Example 2 is not fully-connected because computers 2 and 0 cannot communicate.
    There are other such pairs of computers that cannot communicate like 4 and 1, etc..

    A fully-connected network is also considered minimal if it uses as few cables as possible. For example:

    1. the following network is fully-connected AND minimal:
     3
    |
    0--1--2--4


    2. the following network is fully-connected BUT NOT minimal:
        3
    | \
    0--1--2--4

    Example 2 is not minimal because either cable (3,1) or (3,2) or (1,2) is not needed to keep the network fully-connected.

    You are given a computer network that started out as fully-connected and minimal,
    but someone added exactly one extra cable. Your job is to find a cable that can be safely removed, 
    ensuring network is fully-connected and minimal.

    Write a function that takes in number num_computers and a list of cables that connect the computers. 
    Computers have ids from 0 to num_computers - 1. The function should return a cable that can be safely removed. 
    There will be multiple possible cables that can be chosen; you may return any of them.

"""

def extra_cable(num_computers, cables):
    roots = []
    sizes = []

    for idx in range (0, num_computers):
        sizes.append(1)
        roots.append(idx)

    for cable in cables:
        computer_1 , computer_2 = cable
        if not union(roots, sizes, computer_1, computer_2):
            return cable

def find(roots, node):
    if roots[node] == node:
        return node
    found = find(roots, roots[node])
    return found
    
def union(roots, sizes, node_a, node_b):
    root_a = find(roots, node_a)
    root_b = find(roots, node_b)

    if root_a == root_b:
        return False

    if sizes[root_a] > sizes[root_b]:
        roots[root_b] = roots[root_a]
        # merge b into as group 
        sizes[root_a] += sizes[root_b]
    else:
        roots[root_a] = roots[root_b]
        sizes[root_b] = roots[root_a]
    return True
