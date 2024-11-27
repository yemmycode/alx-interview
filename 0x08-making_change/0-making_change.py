#!/usr/bin/python3
"""Module for calculating the minimum number of coins required to meet a target total.
"""

def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to reach a specified total
    using a given set of coin denominations.

    Args:
        coins (list): List of coin denominations available.
        total (int): Target amount to achieve.

    Returns:
        int: Minimum number of coins required to meet the total, or -1 if it is not possible.
    """
    if total <= 0:
        return 0

    sorted_coins = sorted(coins, reverse=True)
    rem = total
    coins_count = 0
    coin_idx = 0
    n = len(coins)

    while rem > 0:
        if coin_idx >= n:
            return -1

        if rem >= sorted_coins[coin_idx]:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1

    return coins_count

