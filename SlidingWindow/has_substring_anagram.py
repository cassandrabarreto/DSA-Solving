""" 
    
Write a function that takes in a string and an anagram. The function 
should return a boolean indicating whether or not the string contains a substring with the same characters 
as the anagram.
You can assume that the string contains no duplicate characters.
You can assume that the anagram contains no duplicate characters.
You can assume that the anagram is not longer than the string.
"""

def has_substring_anagram(s : str, anagram : str) -> bool:
    # Step 1: process first window
    k = len(anagram)
    window_set = set(s[:k])
    anagram_set = set(anagram)

    if window_set == anagram_set:
        return True

    # Shift Window
    for i in range(0, len(s) - k):
        # Remove Training Element
        window_set.remove(s[i])
        # Add leading element
        window_set.add(s[i+k])
        if window_set == anagram_set:
            return True
    return False
