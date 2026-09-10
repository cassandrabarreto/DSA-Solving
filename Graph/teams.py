
""" 
    Write a function, tolerant_teams, that takes in a list of rivalries as an argument. 
    A rivalry is a pair of people who should not be placed on the same team. 
    The function should return a boolean indicating whether or not it is possible to separate people into two teams, without rivals 
    being on the same team. The two teams formed do not have to be the same size.
"""

def tolerant_teams(rivalries):
    graph = convert_edges(rivalries)
    colored = {}

    for node in graph:
        if node not in colored:
            if not is_bipartite(colored, node, False, graph):
                return False
    return True

def is_bipartite(colored, node, current_team_color, graph):
    if node in colored:
        return colored[node] == current_team_color

    colored[node] = current_team_color

    for neighbour in graph[node]:
        if  not is_bipartite(colored, neighbour, not current_team_color, graph):
            return False
    return True

def convert_edges(edges):
    # we need to convert edges into our adjacency list
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














""" 
    
Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

    LRUCache(int capacity) Initialize the LRU cache of size capacity.
    int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
    A key is considered used if a get or a put operation is called on it.

"""

class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()

        # Define left and right dummy heads
        self.left = Node(0,0)
        self.right = Node(0,0)

        # connect them
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self,node):
        prev = self.right.prev
        nxt = self.right
        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev

    def remove(self,node):
        # obtain prev and next
        # in this case prev should be dummy head
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        # If the key exists in dict
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            # reinsert
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        # if key already exists
        if key in self.cache:
            self.remove(self.cache[key])
        # create new node instance
        new_node = Node(key, value)
        # Insert it
        self.cache[key] = new_node
        self.insert(self.cache[key])
        # add it to cache

        # if the capacity is exceeded
        if len(self.cache) > self.capacity:
            # delete the leftmost node before left dummy head (LRU)
            lru_node = self.left.next
            # remove from double linked list
            self.remove(lru_node)
            # delete it from cache
            del self.cache[lru_node.key]





        

