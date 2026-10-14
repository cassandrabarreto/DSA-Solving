""" 
Write a function that takes in a list of numbers and a size k as arguments. 
The function should return the maximum sum of subarrays that contain exactly k elements.
You can assume that k is less than or equal to the length of the input list.    
"""
#max_subarray_sum_size_k([4, 2, 1, -9, 8, 4, 3], 3) # -> 15
# [8,4,3] is the subarray of size 3 with the maximal sum

def max_subarray_sum_size_k(nums, k):
    addition = sum(nums[:k])
    max_sum = float('-inf')
    max_sum = addition

    for i in range(0, len(nums) - k):
        # remove trailing element
        addition -= nums[i]
        # add leading element
        addition += nums[i + k]

        max_sum = max(addition, max_sum)
    return max_sum



"""
Write a function that takes in a list of numbers and a size k as arguments. 
The function should return the maximum product of subarrays that contain exactly k elements.
You can assume that k is less than or equal to the length of the input list.
You can assume that numbers of the list are non-zero
"""
#max_subarray_product_size_k([4, 2, 1, -9, 8, 2, 3], 3) # -> 48
# [8,2,3] is the subarray of size 3 with the maximal product
import math
def max_subarray_product_size_k(nums, k):
    current_product = math.prod(nums[:k])
    max_product = current_product

    for i in range(0, len(nums) - k):
        # remove trailing element
        current_product /= nums[i]
        # add leading element
        current_product *= nums[i+k]

        max_product = max(current_product, max_product)
    return max_product




""" 
Write a function that takes in a list of numbers, a target sum, and a size k as arguments. 
The function should return the number of subarrays of size k that sum to the target.
You can assume that k is less than or equal to the length of the input list.    
"""

def subarray_target_sum_size_k(nums, target, k):
    current_window = nums[:k]
    addition = sum(current_window)
    
    count = 1 if addition == target else 0

    for i in range(0, len(nums)- k):
        # will remove trailing element
        addition -= nums[i]
        # add leading element
        addition += nums[i+k]

        if addition == target:
            count +=1
    return count 
        


""" 
    
Write a function that takes in a string and an anagram
The function should return a boolean indicating whether or 
not the string contains a substring with the same characters as the anagram.
You can assume that the string contains no duplicate characters.
You can assume that the anagram contains no duplicate characters.
You can assume that the anagram is not longer than the string.
"""
def has_substring_anagram(s, anagram):
    # process first window
    k = len(anagram)
    anagram_set = set(anagram)
    window_set = set(s[:k])
    if window_set == anagram_set:
        return True

    for i in range (0, len(s)-k):
        window_set.remove(s[i])
        window_set.add(s[i + k])
        if anagram_set == window_set:
            return True
    return False



""" 
    
Write a function that takes in a string and an anagram. 
The function should return the number of substrings that appear in the 
string that have the same characters as the anagram.
You can assume that the anagram is not longer than the string.
"""

from collections import Counter
def count_substring_anagrams(s, anagram):
    k = len(anagram) 
    window_counter = Counter(s[:k])
    anagram_counter = Counter(anagram)

    count = 1 if window_counter == anagram_counter else 0
    
    for i in range(0, len(s) - k):
        window_counter[s[i]] -= 1
        window_counter[s[i+k]] += 1
 
        if window_counter == anagram_counter:
            count += 1
    return count






"""
Write a function that takes in a list and a target sum. 
The function should return the start and end indices (inclusive) of a subarray that sums to the target.
You can assume that the elements of the list are nonnegative.
You can assume that there is exactly one subarray that sums to the target.
"""
def find_subarray_sum(nums, target_sum):
    start = 0
    addition = 0
    
    for end in range(0, len(nums)):
        addition += nums[end]
        while addition  > target_sum:
            addition -= nums[start]
            start += 1
        if addition == target_sum:
            return (start, end)
        




""" 
Write a function that takes in an list and a target sum. 
The function should return the length of the longest subarray that sums to the target.
You can assume that the elements of the list are nonnegative.
If there is no subarray that sums to the target, then return -1.
"""

def longest_subarray_sum(nums, target_sum):
    current_window = 0
    max_lenght = 0

    for end in range(0, len(nums)):
        current_window += nums[end]
        
        pass



""" 
Write a function that takes in an list and a target sum. 
The function should return the length of the longest subarray that sums to the target.
You can assume that the elements of the list are nonnegative.
If there is no subarray that sums to the target, then return -1.
"""
def longest_subarray_sum(nums, target_sum):
    longest_addition = 0
    addition = 0
    start = 0

    for end in range(0, len(nums)):
        # add leading element
        addition += nums[end]
        while addition > target_sum:
            # remove trailing element
            addition -= nums[start]
            start += 1
        if addition == target_sum:
            longest_addition = max(end - start + 1,  longest_addition)
    return -1 if longest_addition == 0 else longest_addition







""" 
Write a function that takes in a string as an argument. The function should 
return the length of the longest substring that consists of only unique characters.
"""
from collections import Counter
def longest_unique_substring(s):
    start = 0
    longest_len = 0
    window = Counter()

    for end in range(0, len(s)):
        # add lead elem
        lead_elem = s[end]
        window[lead_elem] += 1
        # constraint violation
        while window[lead_elem] > 1:
            # remove start elem
            trailing_elem = s[start]
            window[trailing_elem] -= 1
            start += 1
            if window[trailing_elem] == 0:
                del window[trailing_elem]
        longest_len = max(longest_len, end - start + 1)
    return longest_len



""" 
Write a function that takes in a string as an argument. The function should return the 
length of the longest substring that consists of 2 distinct characters
"""
from collections import Counter
def longest_two_char_substring(s):
    start = 0
    max_len = 0
    window = Counter()

    for end in range(0, len(s)):
        # lead
        lead_elem = s[end]
        window[lead_elem] += 1

        # constraint
        while len(window) > 2:
            # trailing elem
            trail_elem = s[start]
            window[trail_elem] -= 1
            start += 1 

            if window[trail_elem] == 0:
                del window[trail_elem]
        if len(window) == 2:
            max_len = max(max_len, end - start + 1)
    return max_len

""" 
    Write a function that takes in a string containing only '0's and '1's.
    The function should return the length of the longest consecutive streak of 
    '1's possible if you are allowed to change at most one '0' into a '1'.
"""

def max_ones_with_single_flip(s):
    start = 0
    longest_len = 0
    number_zeros = 0

    for end in range(0, len(s)):
        # lead
        lead = s[end]
        if lead == "0":
            number_zeros += 1 
        while number_zeros > 1:
            if s[start] == "0":
                number_zeros -= 1
            start += 1
        longest_len = max(longest_len, end - start + 1)
    return longest_len














""" 
Write a function that takes in a string containing only '0's and '1's. The function should 
return the length of the longest consecutive streak of '1's 
possible if you are allowed to change at most one '0' into a '1'.
"""
def max_ones_with_single_flip(s):
    max_len = 0
    start = 0
    number_zeros = 0

    for end in range(0, len(s)):
        # leading elem
        lead = s[end]
        if lead == "0":
            number_zeros += 1
        # constraint violation
        while number_zeros > 1:
            trail = s[start]
            if trail == "0":
                number_zeros -= 1
            start += 1
        max_len = max(max_len, end - start + 1)
    return max_len




""" 
Write a function that takes in an array of positive integers and a target product. 
The function should return the number of subarrays that have a total product strictly less than the target.
"""

def count_subarray_product(nums, target_product):
    start = 0
    subarr_num = 0
    prod = 1

    for end in range(0, len(nums)):
        prod *= nums[end]
        while prod >= target_product and start <= end:
            prod /= nums[start]
            start += 1
        subarr_num += end - start + 1
    return subarr_num


""" 
Write a function that takes in a string and a number k. 
The function should return the number of substrings that consist of at most k distinct characters.    
"""
from collections import Counter
def count_substring_at_most_k_distinct(s, k):
    start = 0
    current_window = Counter()
    substr_num = 0

    for end in range(0, len(s)):
        # lead
        lead = s[end]
        current_window[lead] += 1

        while len(current_window) > k:
            trail = s[start]
            current_window[trail] -= 1
            start += 1
            if current_window[trail] == 0:
                del current_window[trail]
        substr_num += end - start + 1
    return substr_num



""" 
Write a function that takes in a string and a number k. 
The function should return the number of substrings that consist of exactly k distinct characters.
"""
from collections import Counter
def count_at_most(s, k):
    start = 0
    window = Counter()
    subs_num = 0
        
    for end in range(0, len(window)):
        # lead element
        lead = s[end]
        window[lead] += 1

        while len(window) > k:
            # trailing
            trail = s[start]
            window[trail] -= 1
            if window[trail] == 0:
                del window[trail]
            start += 1
        if len(window) == k:
            subs_num += end - start + 1
    return subs_num

def count_substring_exactly_k_distinct(s,k):
    return count_at_most(s,k) - count_at_most(s, k- 1)