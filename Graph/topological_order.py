""" 
    Write a function, topological_order, that takes in a dictionary representing 
    the adjacency list for a directed-acyclic graph. The function should return a 
    list containing the topological-order of the graph.

    The topological ordering of a graph is a sequence where "parent nodes" appear before their "children" within the sequence.  

    topological_order({
    "a": ["f"],
    "b": ["d"],
    "c": ["a", "f"],
    "d": ["e"],
    "e": [],
    "f": ["b", "e"],
    }) # -> ['c', 'a', 'f', 'b', 'd', 'e']
"""

def topological_order(graph):
    parent_numbers = dict()
    # create dictionary with each node
    for node in graph:
        parent_numbers[node] = 0

    # Count each node's parents
    for node in graph:
        for child in graph[node]:
            parent_numbers[child] += 1

    ready = []
    for node in graph:
        if parent_numbers[node] == 0:
            ready.append(node)

    order = []

    while ready:
        node = ready.pop()
        order.append(node)                                                                                                                                                                                                                                                                                                                                              
        for child in graph[node]:
            parent_numbers[child] -= 1
            if parent_numbers[child] == 0:
                ready.append(child)
    return order


