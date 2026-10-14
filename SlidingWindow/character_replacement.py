""" 
    You are given a string s consisting of only uppercase english characters and an integer k. 
    You can choose up to k characters of the string and replace them with any other uppercase English character.

    After performing at most k replacements, return the length of the longest 
    substring which contains only one distinct character.

    Example 1:
        Input: s = "XYYX", k = 2
        Output: 4

"""
from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        collection = Counter()
        max_lenght = 0
        start = 0

        for end in range (0, len(s)):
            trailing_element = s[end]
            collection[trailing_element] += 1

            # we want to check if we can replace k times at most
            while (end - start + 1 ) - max(collection.values()) > k:
                lead_element = s[start]
                collection[lead_element] -= 1

                if collection[lead_element] == 0:
                    del collection[lead_element]
                start += 1
            max_lenght = max(max_lenght, end - start + 1)
        return max_lenght

