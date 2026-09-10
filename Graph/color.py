""" 
    
    Write a function, can_color, that takes in 
    a dictionary representing the adjacency list of an undirected graph.
    The function should return a boolean indicating whether or not 
    it is possible to color nodes of the graph using two colors
    in such a way that adjacent nodes are always different colors.

    For example, given this graph:

    x-y-z

    It is possible to color the nodes by using red for x and z, 
    then use blue for y. So the answer is True.

    For example, given this graph:

        q
       / \
      s - r

    It is not possible to color the nodes without making two 
    adjacent nodes the same color. So the answer is False.

"""

def can_color(graph):

    coloring = {}
    
    for node in graph:
        if node not in coloring:
            if not validate(graph, node, coloring, False):
                return False
    return True

def validate(graph, node, coloring, current_color):
    # Base Case
    if node in coloring:
        return coloring[node] == current_color
    
    coloring[node] = current_color

    for neighbour in graph[node]:
        if not validate(graph, neighbour, coloring, current_color):
            return False
    return True
            