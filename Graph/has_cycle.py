
"""
Write a function, has_cycle, that takes in an object representing the adjacency list of a directed graph.
The function should return a boolean indicating whether or not the graph contains a cycle.
"""

def has_cycle(graph: dict[str, list[str]]) -> bool:
    visited = set()
    visiting = set()

    for node in graph:
        if cycle_detect(graph, node, visited, visiting):
            return True
    return False    

def cycle_detect(graph :  dict[str, list[str]], node: str, visited: set, visiting: set):
    # Base Case #1: If we encounter with a node that already has been visited
    if node in visited:
        return False
    # Base Case #2: If we encounter with a node that is in current path, there is a cycle.
    if node in visiting:
        return True
    # Currently visiting node
    visiting.add(node)

    # Recursive step over neigh
    for neighbour in graph[node]:
        if cycle_detect(graph, neighbour, visited, visiting):
            return True
    # Update status from visiting to visited
    visiting.remove(node)
    visited.add(node)
    return False