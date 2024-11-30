#!/usr/bin/python3
"""Module for calculating the fewest number of coins needed for a total.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet the total amount.

    Args:
        coins (list): List of integers representing coin denominations.
        total (int): The target amount to achieve.

    Returns:
        int: Minimum number of coins required to achieve the total.
             Returns 0 if total is 0 or less.
             Returns -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order for efficient computation
    coins.sort(reverse=True)

    rem = total  # Remaining amount to be met
    coins_count = 0  # Count of coins used

    for coin in coins:
        if rem <= 0:
            break
        # Use as many of the current denomination as possible
        count = rem // coin
        coins_count += count
        rem -= coin * count

    return coins_count if rem == 0 else -1
