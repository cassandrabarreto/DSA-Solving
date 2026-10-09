""" 
    Given an integer array nums and an integer k, return the k most frequent elements within the array.
    The test cases are generated such that the answer is always unique.
    You may return the output in any order.

    Example 1:
    Input: nums = [1,2,2,3,3,3], k = 2  
    Output: [2,3]    
"""
from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = Counter(nums)
        my_heap = []
        numbers_count = hash_map.items()
        # to find biggest nums
        for num, count in numbers_count:
            heapq.heappush(my_heap, (count,num))
            if len(my_heap) > k:
                heapq.heappop(my_heap)
        result = []
        for count, number in my_heap:
            result.append(number)
        return result


