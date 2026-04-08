""" 
    
Write a function, intersection_with_dupes, that takes in two lists, a,b, as arguments. 
The function should return a new list containing elements that are common to both input lists. 
sThe elements in the result should appear as many times as they occur in both input lists.

"""
def intersection_with_dupes(a, b):
    a_dict = {}
    b_dict = {}

    num = 0

    final_result = []

    for i in a:
        if i in a_dict:
            a_dict[i] += 1
        else:
            a_dict[i] = 1 

    for i in b:
        if i in b_dict:
            b_dict[i] += 1
        else:
            b_dict[i] = 1 

    for key , value in a_dict.items():
        if key in b_dict:
            num = min(value, b_dict[key])
            for i in range(0, num):
                final_result.append(key)
    return final_result


print(intersection_with_dupes(
  ["a", "b", "c", "b"], 
  ["x", "y", "b", "b"]
)) # -> ["b", "b"]
