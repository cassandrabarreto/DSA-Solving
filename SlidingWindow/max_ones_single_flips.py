"""
Write a function that takes in a string containing only '0's and '1's. The function should return the 
length of the longest consecutive streak of 
'1's possible if you are allowed to change at most one '0' into a '1'.
"""

#max_ones_with_single_flip("10110110") # -> 5
# flipping the second 0 will give us the longest streak of 1se

# 1 0 11
def max_ones_with_single_flip(s):
    # define start pointer set to 0
    start = 0
    longest = 0
    window_zeros = 0

    for end in range(0, len(s)):
        # leading element
        lead = s[end]
        if lead == "0":
            window_zeros += 1
        # constraint violation
        while window_zeros > 1:
            # shrink window
            if s[start] == "0":
                window_zeros  -= 1 
            start += 1
        longest = max(end - start + 1, longest)
    return longest