#!/usr/bin/python3
"""Module defining isWinner function."""


def isWinner(x, nums):
    """Function to get who has won in prime game"""
    mariaWinsCount = 0
    benWinsCount = 0

    for num in nums:
        roundsSet = list(range(1, num + 1))
        primesSet = primes_in_range(1, num)

        if not primesSet:
            benWinsCount += 1
            continue

        isMariaTurns = True

        while(True):
            if not primesSet:
                if isMariaTurns:
                    benWinsCount += 1

