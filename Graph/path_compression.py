""" 
    Write a function, countComponents, that takes in a number of nodes (n) and a list of edges for       an undirected graph. 
    In the graph, nodes are labeled from 0 to n - 1. 
    The function should return the number of connected components in the given graph.
"""

def count_components(n, edges):
    # when using unify by size we need two arrays
    sizes = []
    roots = []

    for index in range(0, n):
        roots.append(index)

    for i in range(0,n):
        sizes.append(1)

    for edge in edges:
        node_a , node_b = edge
        union(roots, sizes, node_a, node_b)

    count = 0
    for i in range(len(roots)):
        if i == roots[i]:
            count += 1
    return count

def find(roots, node):
    if roots[node] == node:
        return node
    found = find(roots, roots[node])
    roots[node] = found
    return found

def union(sizes,roots, node_a, node_b):
    root_a = find(roots, node_a)
    root_b = find(roots, node_b)

    if root_a == root_b:
        return

    if sizes[root_a] > sizes[root_b]:
        # add elems root as root
        # then merge b in root A;s grooup
        roots[root_b] = root_a
        sizes[root_a] += sizes[root_b]
    else:
        roots[root_a] = root_b
        sizes[root_b] += sizes[root_a]