""" 
    
Write a function that takes in a string as an argument. 
The function should return the length of the longest substring 
that consists of only unique characters.
"""

#longest_unique_substring("abcabcqbb") # -> 4
# 'abcq' is the longest substring with unique characters and its length is 4\
from collections import Counter
def longest_unique_substring(s):
    start = 0
    current_window = Counter()
    longest = 0

    for end in range (0, len(s)):
        leading_char = s[end]
        current_window[leading_char] += 1 

        while current_window[leading_char] > 1:
            # get trailing element
            trailing_char = s[start]
            current_window[trailing_char] -= 1
            start += 1 
        longest = max(end - start + 1, longest)
    return longest
        