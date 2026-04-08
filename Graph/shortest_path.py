
""" 
    Write a function, shortest_path, that takes in a list of edges for an undirected graph and
    two nodes (node_A, node_B). The function should return the length of the shortest path between
    A and B. Consider the length as the number of edges in the path, not the number of nodes. 
    If there is no path between A and B,
    then return -1. You can assume that A and B exist as nodes in the graph.

"""
from collections import deque
def shortest_path(edges, node_A, node_B):
    graph = convert(edges)
    visited = set()
    return find_shortest_path(graph, node_A, node_B, visited)


def find_shortest_path(graph, src, dst, visited):
    queue = deque([(src, 0)])

    if src in visited:
            return -1

    visited.add(src)
    while queue:
        current , distance = queue.popleft()

        if current == dst:
            return distance
        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append((neighbour, distance + 1))
                visited.add(neighbour)
    return -1

def convert(edges):
    graph = {}
    for edge in edges:
        a , b = edge[0], edge[1]

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph
