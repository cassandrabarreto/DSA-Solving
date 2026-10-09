""" 
Write a function that takes in a string and a number k. 
The function should return the number of substrings that consist of 
at most k distinct characters.
"""
from collections import Counter
def count_substring_at_most_k_distinct(s, k):
    start = 0
    global_count = 0
    current_counter = Counter()

    for end in range(0, len(s)):
        # get lead element
        lead = s[end]
        current_counter[lead] += 1 

        # Constraint violation handling
        while len(current_counter) > k:
            # trailing
            trailing = s[start]
            # decrease  start pointer by 1 
            current_counter[trailing] -= 1 
            start += 1 
            # If the element equals to zero, remove it from the counter.
            if current_counter[trailing] == 0:
                del current_counter[trailing]
        global_count += end - start + 1 
    return global_count
        





