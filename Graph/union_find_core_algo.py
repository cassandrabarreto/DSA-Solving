"""
    Write a function, count_components, that takes in a number of nodes (n) and a 
    list of edges for an undirected graph. In the graph, nodes are labeled from 0 to n - 1. 
    The function should return the number of connected components in the given graph.

    count_components(7, [
        (0, 2),
        (1, 0),
        (4, 3),
        (2, 5),
        (3, 6)
    ])
"""
def count_components(n, edges):
    roots = []

    # Every node starts as a leader
    for i in range (0, n):
        roots.append(i)
    # For each edge, call union
    for edge in edges:
        node_a , node_b = edge  
        union(roots, node_a, node_b)


    # Counting the number of leaders will tell the number of connected components
    # Leader is a node that holds a value equal to the array's index
    count = 0
    for i in range(0, len(roots)):
        if i == roots[i]:
            count += 1
    return count

def find(roots, node):
    # If elem in the node index is the same as the node, return team's leader.
    # Otherwise, keep looking for it.
    if node == roots[node]:
        return node
    return find(roots, roots[node])

def union(roots, node_a, node_b):
    # Find each node's leader
    root_a = find(roots, node_a)
    root_b = find(roots, node_b)
    roots[root_b] = root_a
    