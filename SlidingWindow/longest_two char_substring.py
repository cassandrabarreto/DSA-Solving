
"""
Write a function that takes in a string as an argument. 
The function should return the length of the longest substring that consists of 2 distinct characters
"""
#longest_two_char_substring("xyzyyx") # -> 4
# 'yzyy' is the longest substring of 2 distinct characters and its length is 4
from collections import Counter
def longest_two_char_substring(s: str) -> int:
    start = 0
    longest = 0
    window_counter = Counter()

    for end in range (0, len(s)):
        # shift end pointer and add it to counter
        # leading element
        leading_elem = s[end]
        window_counter[leading_elem] += 1
        longest += 1

        # Constraint violation handling (If the window has more than 2 chars)
        while len(window_counter) > 2:
            # shrink window
            # get trailing element
            trailing_elem = s[start]
            window_counter[trailing_elem] -= 1
            # If a key gets to zero, we should delete it from the Counter. 
            if window_counter[trailing_elem] == 0:
                del window_counter[trailing_elem]
        # We only retrieve longest if we have exactly two characters.
        if len(window_counter) == 2:
            longest = max(end )
    return longest

