""" 
Write a function, pairs, that takes in a list as an argument. The function should return a list containing all unique pairs of elements.

You may return the pairs in any order and the order of elements within a single pair does not matter.

You can assume that the input list contains unique elements.

pairs(["a", "b", "c"]) # ->
# [
#    ["a", "b"],
#    ["a", "c"],
#    ["b", "c"]
# ]
"""

def pairs(chars):
    pairs = []
    for i in enumerate(chars):
        for j in pairs[i+1]:
            pairs.append([i,j])
    return pairs


def pairs(elements):
    pairs = []
    for i in range (0, len(elements)):
        for j in range(i+1, len(elements)):
            pair = [elements[i], elements[j] ]
            pairs.append(pair)
    return pairs
