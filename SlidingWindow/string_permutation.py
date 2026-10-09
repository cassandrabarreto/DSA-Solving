""" 
    You are given two strings s1 and s2.

    Return true if s2 contains a permutation of s1, or false otherwise. 
    That means if a permutation of s1 exists as a substring of s2, then return true.

    Both strings only contain lowercase letters.

    Example 1:

        Input: s1 = "abc", s2 = "lecabee"

        Output: true

"""
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # we first need to process first window, this a k variable problem
        k = len(s1)
        string1_counter = Counter(s1)
        # we need a window which can be a set
        current_window = Counter(s2[:k])

        if current_window == string1_counter:
            return True
        
        for i in range (0, len(s2)-k):
            # remove trailing element
            current_window[s2[i]] -= 1

            # add following elem
            current_window[s2[i + k]] += 1

            if current_window[s2[i + k]] == 0:
                del current_window[s2[i + k]]

            if current_window == string1_counter:
                return True
        return False

