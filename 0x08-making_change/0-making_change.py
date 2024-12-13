#!/usr/bin/python3
""" This module determines the fewest number of coins
needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Parameters:
        coins (list): A list of integers representing coin denominations.
        total (int): The target amount.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for t in range(coin, total + 1):
            dp[t] = min(dp[t], dp[t - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
