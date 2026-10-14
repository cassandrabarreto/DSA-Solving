""" 
    Given a string s, find the length of the longest substring without duplicate characters.
    A substring is a contiguous sequence of characters within a string.

    Neetcode

    Example 1:
        Input: s = "zxyzxyz"
        Output: 3
"""

from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        mx_lenght = 0
        chars = Counter()

        for end in range(0, len(s)):
            nxt_elem = s[end]
            chars[nxt_elem] += 1
            # the constraint is violated bc we expect unique characters
            while chars[nxt_elem] > 1:
                # obtain start
                start_elem = s[start]
                chars[start_elem] -= 1

                if chars[start_elem] == 0:
                    del chars[start_elem]
                start += 1
            mx_lenght = max(mx_lenght, end - start + 1)
        return mx_lenght
            