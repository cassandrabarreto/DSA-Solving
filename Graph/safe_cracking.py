""" 
    Oh-no! You forgot the number combination that unlocks your safe. Luckily, you knew that
    you'd be forgetful so you previously wrote down a
    bunch of hints that can be used to determine the correct combination.
    Each hint is a pair of numbers 'x, y' that indicates you must enter 
    digit 'x' before 'y' (but not necessarily immediately before y).

    The keypad on the safe has digits 0-9. 
    You can assume that the hints will generate exactly one working combination and 
    that a digit can occur zero or one time in the answer.

    Write a function, safe_cracking, that takes in a list of hints 
    as an argument and determines the combination that will unlock the safe. 
    The function should return a string representing the combination.    

"""

def safe_cracking(hints):
    graph = convert_to_graph(hints)
    digits_nums = {}

    # we should build our edge parent-child count
    for node in graph:
        digits_nums[node] = 0

    # count parents for each child
    for node in graph:
        for child in graph[node]:
            digits_nums[child] += 1

    # Prepare ready array
    ready = []

    for node in graph:
        if digits_nums[node] == 0:
            ready.append(node)

    final_password = ""
    # Now its the moment to process non parent nodes
    while ready:
        # retrieve the node from the ready array
        node = ready.pop()
        # add the node into the final password
        final_password += str(node)
        # it is now needed to decrease child's edge with parent to properly order them in a sequence
        for child in graph[node]:
            digits_nums[child] -= 1
            if digits_nums[child] == 0:
                ready.append(child)
    return final_password
            

def convert_to_graph(edges):
    graph = {}

    for edge in edges:
        a , b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
    return graph  


assert safe_cracking([(7,1), (1,8), (7,8)]) == "718"
assert safe_cracking([(1,2), (2,3), (3,4)]) == "1234"