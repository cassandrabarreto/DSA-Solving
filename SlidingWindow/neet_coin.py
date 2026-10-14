""" 
    You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
    You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
    Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

    Example 1:

        Input: prices = [10,1,5,6,7,1]

        Output: 6
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        start = 0
        for end in range (0, len(prices) ):
            while prices[end] < prices[start]:
                start += 1
            max_profit = max(prices[end] - prices[start], max_profit)
        return max_profit
        