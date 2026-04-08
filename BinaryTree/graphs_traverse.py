graph = {
    "a" : ["b", "c"],
    "f" : ["x", "a"]
}


def depth_first_print_iterative(graph, start):
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

from collections import deque 
def breadth_first_print(graph, start):
    queue = deque([start])

    while queue:
        current = queue.popleft()
        print(current)

        for neighbour in graph[current]:
            queue.append(neighbour)



"""
Write a function, has_path, that takes in a dictionary representing the adjacency 
list of a directed acyclic graph and two nodes (src, dst). The function should return a boolean indicating whether or not there exists 
a directed path between the source and destination nodes.

"""

# BFS Version
from collections import deque
def has_path(graph, src, dst):
    queue = deque([src])

    while queue:
        current = queue.popleft()

        if current == dst:
            return True

        for neighbour in graph[current]:
            queue.append(neighbour)
    return False


# DFS Version
def has_path(graph, src, dst):
    stack = [src]

    while stack:
        current = stack.pop()

        if current == dst:
            return True

        for neighbour in graph[current]:
            stack.append(neighbour)
    return False


def has_path(graph, src, dst):
    #Base Case
    if src == dst:
        return True
    
    for neighbour in graph[src]:
        if has_path(graph, src, dst) == True:
            return True
        else:
            return False
        



def undirected_path(edges, node_A, node_B):
    graph = build_graph(edges)
    return _undirected_path(graph, node_A, node_B)

def build_graph(edges):

    """ 
    edges = [
        ('i', 'j'),
        ('k', 'i'),
        ('m', 'k'),
        ('k', 'l'),
        ('o', 'n')
    ]
    """
    graph = {}

    for edge in edges:
        a , b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph

from collections import deque
def _undirected_path(graph, src, dst):
    queue = deque([src])
    visited = {src}

    while queue:
        current = queue.popleft()
        if current == dst:
            return True
        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return False







def undirected_path(edges, node_A, node_B):
    graph = convert_to_graph(edges) 
    print(graph)
    return _undirected_path(graph, node_A, node_B)

def convert_to_graph(edges):
    graph = {}
    for edge in edges:
        # extract tuples values
        a , b = edge
        # If the node is not in the graph, add it.
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        
        # Symmetrical adding of nodes
        graph[a].append(b)
        graph[b].append(a)
    return graph 

from collections import deque
def _undirected_path(graph, src , dst):
    queue = deque([ src ])
    visited = { src }

    while queue:
        #Pop element
        current = queue.popleft()

        #Check if its the same as dst
        if current == dst:
            return True
        # for each neighbour for the current node
        for neighbour in graph[current]:
            # If we have not visited the current node, add it to visited and go through each of its neighbours
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    print(visited)
    return False
            
        


from collections import deque
def connected_components_count(graph):
    queue = deque([])





def undirected_path(edges, node_A, node_B):
    graph = convert_to_graph(edges)
    return _undirected_path(graph)

def convert_to_graph(edges):
    """
    edges = [
        ('i', 'j'),
        ('k', 'i'),
        ('m', 'k'),
        ('k', 'l'),
        ('o', 'n')
    ]
    """
    graph = {}

    for edge in edges:
        a , b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

from collections import deque
def _undirected_path(graph, src, dst):
    queue = deque([src])
    visited = {src}

    while queue:
        current = queue.popleft()

        if current == dst:
            return True

        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                
    return False




"""
Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. 
The function should return the number of connected components within the graph.

"""
from collections import deque
def connected_components_count(graph):
    visited = set()
    count = 0

    # Iterate over each node in graph
    for node in graph:
        if explore(graph, node, visited):
            count += 1 
    return count

def explore(graph, src, visited):
    queue = deque([src])

    # We have visited the node already. return flase
    if src in visited:
        return False

    # Traverse through each neighbour of the src node
    while queue:
        current = queue.popleft()
        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
    return True


def connected_components_count(graph):
    visited = set()
    count = 0

    # Iterate over each node in graph
    for node in graph:
        if explore(graph, node, visited):
            count += 1 
    return count

def explore(graph, src, visited):
    # Base Case
    if src in visited:
        return False
    
    visited.add(src)

    # Recursive Call
    for neighbour in graph[src]:
        explore(graph, neighbour, visited)
    return True




from collections import deque
def largest_component(graph):
    visited = set()
    counts = []

    for node in graph:
        count = explore(graph, node, visited)
        counts.append(count)
    
    if counts:
        return max(counts)
    else:
        return 0

def explore(graph, src, visited):
    queue = deque([src])
    count = 1
    if src in visited:
        return 0
    visited.add(src)
    
    while queue:
        current = queue.popleft()

        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
                count += 1
    return count


def traverse(graph, start):
    stack = [start]
    visited = set()
    nodes = []


    while stack:
        current = stack.pop()
        nodes.append(current)
        visited.add(current)

        for neighbour in graph[current]:
            if neighbour not in visited:
                stack.append(neighbour)
            
    return nodes



""" 
    Write a function, has_path, that takes in a dictionary representing the adjacency list of
    a directed acyclic graph and two nodes (src, dst). The function should return a boolean
    indicating whether or not there exists a 
    directed path between the source and destination nodes.

"""

def has_path(graph, src, dst):
    
    if src == dst:
        return True

    for neighbour in graph[src]:
        if has_path(graph, src, dst):
            return True
    return False


def has_path(graph, src, dst):
    stack = [src]

    while stack:
        current = stack.pop()
        if current == dst:
            return True

        for neighbour in graph[current]:
            stack.append(neighbour)
    return False


def has_path(graph, src, dst):
    #Base Case
    if src == dst:
        return True

    for neighbour in graph[src]:
        if has_path(graph, neighbour, dst):
            return True
    return False





""" 
    Write a function, undirected_path, that takes in a list of edges for 
    an undirected graph and two nodes (node_A, node_B). The function should return a boolean 
    indicating whether or 
    not there exists a path between node_A and node_B.
"""

def undirected_path(edges, node_A, node_B):
    graph = convert_to_graph(edges)
    return explore(graph, node_A, node_B)

def convert_to_graph(edges):
    graph = {}
    for edge in edges:
        # retrieve tuples elements
        a , b = edge
        #Check if the node exists in the adjacency list
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

from collections import deque
def explore(graph, src, dst):
    queue = deque([src])
    visited = set(src)

    while queue:
        current = queue.popleft()
    
        if current == dst:
            return True

        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
    return False



""" 
    Write a function, connected_components_count, 
    hat takes in the adjacency list of an undirected graph. 
    The function should return the number of connected components within the graph.
"""
def connected_components_count(graph):
    count = 0
    visited = set()
    for node in graph:
        if explore_neighbours(graph, node, visited):
            count += 1 
    return count


from collections import deque
def explore_neighbours(graph, src, visited):
    queue = deque([src])

    if src in visited:
        return False
    
    while queue:
        current = queue.popleft()

        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
    return True



""" 
    Write a function, largest_component, that takes in the adjacency list of an undirected graph. 
    The function should return the size of the largest connected component in the graph.

"""
def largest_component(graph):
    visited = set()
    counts = []
    for node in graph:
        count = count_components(graph, node, visited)
        counts.append(count)

    if counts:
        return max(counts)
    else:
        return 0
    

from collections import deque
def count_components(graph, src, visited):
    queue = deque([src])
    counter = 1

    if src in visited:
        return 0

    while queue:
        current = queue.popleft()
        
        visited.add(src)
        
        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                counter += 1
    return counter

""" 
Write a function, hasPath, that takes in an object representing the adjacency 
list of a directed acyclic graph and two nodes (src, dst). 
The function should return a boolean indicating whether or not there
 exists a directed path between the source and destination nodes.

"""

from collections import deque
def has_path(graph, src, dst):
    queue = deque([src])

    while queue:
        current = queue.popleft()

        if current == dst:
            return True
        
        for neighbour in graph[current]:
            queue.append(neighbour)
    return False

def has_path(graph, src, dst):
    # Base Case
    if src == dst:
        return True
    for neighbour in graph[src]:
        if has_path(graph, neighbour, dst):
            return True
    return False




""" 
Write a function, undirected_path, that takes in a list of edges for an
undirected graph and two nodes (node_A, node_B). The function should return a boolean 
indicating whether or not there exists a path between node_A and node_B.
"""
from collections import deque
def undirected_path(edges, node_A, node_B):
    graph = convert(edges)
    visited = set()
    return explore(graph, node_A, node_B, visited)
    

def convert(edges):
    graph = {}
    for edge in edges:
        a , b  = edge

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)
    return graph

def explore(graph, src, dst, visited):
    queue = deque([src])
    visited.add(src)

    while queue:
        current = queue.popleft()

        if current == dst:
            return True

        for neighbour in graph[current]:
            if neighbour  not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
    return False


""" 
    Write a function, connected_components_count, that takes in the adjacency list of an undirected graph.
    The function should return the number of connected components within the graph.
"""
from collections import deque
def connected_components_count(graph):

    if graph is None:
        return 0
    
    visited = set()
    counter = 0

    for node in graph:
        if count_component(graph, node, visited):
            counter += 1
    return counter

def count_component(graph, src, visited):
    queue = deque([src])

    if src in visited:
        return False
    
    visited.add(src)

    while queue:
        current = queue.popleft()

        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
    return True


from collections import deque
def connected_components_count(graph):
    counter = 0
    visited = set()
    for node in graph:
        if count_components(graph, node,  visited):
            c
    return ma

def count_components(graph, current ,visited):
    # Base Case
    if current in visited:
        return False
    visited.add(current)
    
    for neighbour in graph[current]:
        count_components(graph, neighbour, visited)
    return True
    """
    queue = deque([src])

    if src in visited:
        return False
    visited.add(src)
    while queue:
        current = queue.popleft()
        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
    return True
    """


""" 
    Write a function, largest_component, that takes in the adjacency list of an undirected graph.
    The function should return the size of the largest connected component in the graph.


"""

def largest_component(graph):
    visited = set()
    counts = []

    if graph is None:
        return 0

    for node in graph:
        count = get_largest(graph, node, visited)
        counts.append(count)
    if counts is None:
        return 0
    else:
        return max(counts, default=0)


def get_largest(graph, src, visited):
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


def shortest_path(edges, node_A, node_B):
    graph = convert(edges)
    

def convert(edges):
    graph = {}
    for edge in edges:
        a , b = edge[0], edge[1]

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].appenda(a)
    return graph

def find_shortest()