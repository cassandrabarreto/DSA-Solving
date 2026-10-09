""" 
    Write a function, provinceSizes, that takes in a number of cities n and a list of roads which connect cities. 
    Roads can be traveled in both directions. Cities are named from 0 to n.

    A "province" is a group of 1 or more cities that are connected by roads. The "size" of a province is the number of cities 
    that make up that province.

    Your function should return a list containing the sizes of the provinces. You may return the result in any order.
    Solve this using Union-Find.
"""
def province_sizes(n, roads):
    # we need to create our sizes array and the same thing for out roots array
    roots = []
    sizes = []
    # cities are nodes
    # roads are edges
    for idx in range (0, n):
        roots.append(idx)
    # start count by 1 for each size
    for idx in range(0, n):
        sizes.append(1)     

    for edge in roads:
        node_a , node_b = edge
        union(roots, sizes, node_a, node_b)   

    final_result = []

    # for each root count the size
    for idx in range (len(roots)) :
        if roots[idx] == idx:
            # increment final result by including the size if the node is a root.
            size = sizes[idx]
            final_result.append(size)
    return final_result

def find(roots, node):
    if node == roots[node]:
        return node
    found = find(roots, roots[node])
    return found

def union(roots, sizes, node_a, node_b):
    root_a = find(roots, node_a)
    root_b = find(roots, node_b)

    if root_a == root_b:
        return  

    # If A group's bigger than B's group
    if sizes[root_a] > sizes[root_b]:
        # merge b into A group's an increment's A's size
        roots[root_b] = root_a
        sizes[root_a] += sizes[root_b]
    else:
        roots[root_a] = root_b
        sizes[root_b] += sizes[root_a]

