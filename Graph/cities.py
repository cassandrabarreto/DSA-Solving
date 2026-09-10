""" 
Write a function, rare_routing, that takes in a number of cities (n) 
and a list of tuples where each tuple represents a direct road that connects a pair of cities. 
The function should return a boolean indicating whether or not there
 exists a unique route for every pair of cities. A route is a sequence 
 of roads that does not visit a city more than once.

Cities will be numbered 0 to n - 1.

You can assume that all roads are two-way roads. This means 
if there is a road between A and B, then you can use that road to go from A to B or go from B to A. 

rare_routing(4, [
  (0, 1),
  (0, 2),
  (0, 3)
]
"""

def rare_routing(n, roads):
    graph = convert_to_graph(n,roads)
    visited = set()
    valid = verify_route(graph, 0, None, visited)
    return valid and len(visited) == n


def verify_route(graph, node, last_node, visited):
    # If u hit a node that has been visited, return false
    if node in visited:
        return False
    # mark note as visited immediately 
    visited.add(node)

    for neighbour in graph[node]:
        if neighbour != last_node and neighbour and not verify_route(graph, neighbour, node, visited):
            return False
    return True


def convert_to_graph(n, roads):
    graph = {}

    for city in range(n):
        graph[city]= []

    for road in roads:
        a , b = road
        graph[a].append(b)
        graph[b].append(a)
    return graph

