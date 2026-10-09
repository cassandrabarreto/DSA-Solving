
""" 
    Write a function that takes in a string and a number k. 
    The function should return the number of substrings that consist of exactly k distinct characters.
"""
from collections import Counter
def at_most_k(s: str, k: int) -> int:
    start = 0
    substrings_num = 0
    window_counter = Counter()

    for end in range (0, len(s)):
        # lead
        lead = s[end]
        window_counter[lead] += 1 

        while len(window_counter) > k:
            # trail
            trail = s[start]
            window_counter[trail] -= 1 
            start += 1
            if window_counter[trail] == 0:
                del window_counter[trail]
        substrings_num += end - start + 1
    return substrings_num

def count_substring_exactly_k_distinct(s, k):
    return  at_most_k(s,k) - at_most_k(s,k-1)