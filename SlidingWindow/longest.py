""" 
    Write a function that takes in a string as an argument. The function should 
    return the length of the longest substring that consists of only unique characters.
"""
#longest_unique_substring("abcabcqbb") # -> 4
# 'abcq' is the longest substring with unique characters and its length is 4
from collections import Counter
def longest_unique_substring(s):
    longest = 0
    window = Counter()
    # Pointer
    start = 0

    # Start iterating over elements
    for end in range(0, len(s)):
        # Add up 1 to the end to count char
        lead_char = s[end]
        window[lead_char] += 1

        # if condition is not me: (duplicated char)
        while window[lead_char] > 1:
            # shrink the window
            trailing_char = s[start]
            window[trailing_char] -= 1
            start += 1

        # find longest string
        longest = max(end - start + 1, longest)
    return longest
             


""" 
    Write a function that takes in a list of numbers, a target sum, and a size k as arguments. 
    The function should return the number of subarrays of size k that sum to the target.
    You can assume that k is less than or equal to the length of the input list.
"""
#subarray_target_sum_size_k([2, 3, 2, 2, 3, 1, 3, 8, 5, 0, 2, 4], 7, 3) # -> 5
# The 5 subarrays of size 3 whose sum is 7 are:
def subarray_target_sum_size_k(nums, target, k):
    # Create first window
    window = sum(nums[:k])

    global_counter = 1 if window == target else 0

    for i in range (0, len(nums) - k):
        # remove trailing element from window
        window -= nums[i]
        # Add leading element
        window += nums[i+k]
        # Bussiness logic
        if window == target:
            global_counter += 1
    return global_counter


""" 
    
Write a function that takes in a string and an anagram. 
The function should return a boolean indicating whether or not the string contains 
a substring with the same characters as the anagram.
You can assume that the string contains no duplicate characters.
You can assume that the anagram contains no duplicate characters.
You can assume that the anagram is not longer than the string.

"""
#has_substring_anagram("greyhounds", "hoy") # -> True
# the substring "yho" is an anagram of "hoy"



""" 
    
Write a function that takes in a string and an anagram. 
The function should return the number of substrings that appear in 
the string that have the same characters as the anagram.
You can assume that the anagram is not longer than the string.

"""
from collections import Counter
# count_substring_anagrams("tacoctacabcatt", "cat") # -> 4
def count_substring_anagrams(s, anagram):
    k = len(anagram)

    anagram_counter = Counter(anagram)
    window_counter = Counter(s[:k])

    counter = 1 if anagram_counter == window_counter else 0

    # process other windows
    for i in range(0, len(s) - k):
        # trailing element
        trailing_element = s[i]
        # leading element
        leading_element = s[i+k]

        window_counter[trailing_element] -= 1
        window_counter[leading_element] += 1

        if window_counter == anagram_counter:
            counter += 1
    return counter



    