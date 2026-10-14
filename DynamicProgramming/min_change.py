""" 
    Write a function min_change that takes in an amount and a list of coins. 
    The function should return the minimum number of coins required to create the amount.
    You may use each coin as many times as necessary.

    If it is not possible to create the amount, then return -1.
"""

def min_change(amount, coins):
    answer = _min_change_helper(amount, coins, {})
    if answer == float("inf"):
        return -1
    else:
         return answer

def _min_change_helper(amount, coins, memo):
        if amount in memo:
              return memo[amount]
        if amount < 0:
              return float('inf')
        if amount == 0:
              return 0

        min_coins = float('inf')

        for coin in coins:
            num_coins = 1 + _min_change_helper(amount - coin, coins, memo)
            min_coins = min(num_coins, min_coins)
        memo[amount] = min_coins
        return min_coins
        