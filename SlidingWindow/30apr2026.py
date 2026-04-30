

#longest_unique_substring("abcabcqbb") # -> 4
# 'abcq' is the longest substring with unique characters and its length is 4
from collections import Counter
def longest_two_char_substring(s):
    start = 0
    longest = 0

    current_window = Counter()
    
    for end in range(0, len(s)):
        # move end pointer. increment by 1 
        leading = s[end]
        current_window[leading] += 1

        # Violation: more than 2 chars
        while len(current_window) > 2:
            # If there is a violation of the constraint, we will shrink the window by moving start pointer rightwards.
            trailing = s[start]
            current_window[trailing] -= 1
            start += 1 
            
            # if count of the element is zero, remove it from the dict. 
            if current_window[trailing] == 0:
                del current_window[trailing]
        if len(current_window) == 2:
            longest = max(end - start + 1, longest)
    return longest