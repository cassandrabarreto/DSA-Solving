""" 
Write a function that takes in a string and an anagram. 
The function should return the number of substrings that appear in the string that 
have the same characters as the anagram.
You can assume that the anagram is not longer than the string.
"""
from collections import Counter
def count_substring_anagrams(s: str, anagram: str) -> int:
    k = len(anagram)
    
    anagram_counter = Counter(anagram)
    window_counter = Counter(s[:k])
    
    substring_counter = 1 if anagram_counter == window_counter else 0

    for i in range(0, len(s) - k):
        trailing_char = s[i]
        leading_char = s[i+k]

        # Remove trailing character from window
        window_counter[trailing_char] -= 1

        # Add leading element character from window
        window_counter[leading_char] += 1

        if window_counter == anagram_counter:
            substring_counter += 1 
    return substring_counter

