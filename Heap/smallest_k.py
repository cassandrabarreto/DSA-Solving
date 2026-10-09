
""" 
    Write a function that takes in a list of numbers and a value, k. 
    The function should return the k smallest numbers in the list. 
    The resulting list should be ordered from least to greatest.
"""

# Method 1: Sorting 
def k_smallest(nums, k):
    result = []
    sorted_nums = sorted(nums)
    return sorted_nums[:k]

# Method 3: Using Max Heap
import heapq
def k_smallest(nums, k):
    max_heap = []
    for v in nums:
        item = (-v,v)
        heapq.heappush(max_heap, item)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    result = []
    while len(max_heap) > 0:
        item = heapq.heappop(max_heap)
        result.append(item[1])
    return result[::-1]