#!/usr/bin/python3
"""
Prime game implementation.
"""

def isWinner(x, nums):
    """
    Determines the winner of the prime game after x rounds.
    
    :param x: Number of rounds
    :param nums: List of integers representing the maximum numbers for each round
    :return: Name of the player with the most wins or None if there's a tie
    """
    if x < 1 or not nums:
        return None

    # Function to generate prime numbers up to max(nums) using Sieve of Eratosthenes
    def sieve_of_eratosthenes(max_num):
        sieve = [True] * (max_num + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not prime
        for i in range(2, int(max_num**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, max_num + 1, i):
                    sieve[j] = False
        return sieve

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    
    # Precompute the number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Play each round
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

