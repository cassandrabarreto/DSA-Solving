"""
Graph traversal exercises: DFS, BFS, has_path, undirected_path,
connected_components_count, and largest_component.
"""

from collections import deque


# --- Graph Traversal ---

graph = {
    "a": ["b", "c"],
    "b": [],
    "c": [],
    "f": ["x", "a"],
    "x": [],
}


def depth_first_print(graph, start):
    stack = [start]

    while stack:
        current = stack.pop()
        print(current)

        for neighbour in graph[current]:
            stack.append(neighbour)


def depth_first_print_recursive(graph, start):
    print(start)
    for neighbour in graph[start]:
        depth_first_print_recursive(graph, neighbour)


def breadth_first_print(graph, start):
    queue = deque([start])

    while queue:
        current = queue.popleft()
        print(current)

        for neighbour in graph[current]:
            queue.append(neighbour)


# --- Has Path (directed acyclic graph) ---

"""
Write a function, has_path, that takes in a dictionary representing the adjacency
list of a directed acyclic graph and two nodes (src, dst). The function should return a boolean
indicating whether or not there exists a directed path between the source and destination nodes.
"""


def has_path(graph, src, dst):
    if src == dst:
        return True

    for neighbour in graph[src]:
        if has_path(graph, neighbour, dst):
            return True
    return False


# --- Undirected Path ---

"""
Write a function, undirected_path, that takes in a list of edges for an
undirected graph and two nodes (node_A, node_B). The function should return a boolean
indicating whether or not there exists a path between node_A and node_B.
"""


def undirected_path(edges, node_A, node_B):
    graph = build_graph(edges)
    visited = set()
    return _undirected_path(graph, node_A, node_B, visited)


def build_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


def _undirected_path(graph, src, dst, visited):
    queue = deque([src])
    visited.add(src)

    while queue:
        current = queue.popleft()

        if current == dst:
            return True

        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
    return False


# --- Connected Components Count ---

"""
Write a function, connected_components_count, that takes in the adjacency list of an undirected graph.
The function should return the number of connected components within the graph.
"""


def connected_components_count(graph):
    visited = set()
    count = 0

    for node in graph:
        if explore(graph, node, visited):
            count += 1
    return count


def explore(graph, src, visited):
    if src in visited:
        return False

    visited.add(src)

    for neighbour in graph[src]:
        explore(graph, neighbour, visited)
    return True


# --- Largest Component ---

"""
Write a function, largest_component, that takes in the adjacency list of an undirected graph.
The function should return the size of the largest connected component in the graph.
"""


def largest_component(graph):
    visited = set()
    counts = []

    for node in graph:
        count = count_component_size(graph, node, visited)
        counts.append(count)

    return max(counts, default=0)


def count_component_size(graph, src, visited):
    queue = deque([src])
    counter = 1

    if src in visited:
        return 0

    visited.add(src)

    while queue:
        current = queue.popleft()

        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
                counter += 1
    return counter
