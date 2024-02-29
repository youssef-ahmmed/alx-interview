#!/usr/bin/python3
"""Implement Making Change Algorithm"""


def get_min_ignore_none(a, b):
    """Get the min of 2 nums if not None"""
    if not a:
        return b
    if not b:
        return a

    return min(a, b)


def makeChange(coins, total):
    """Making change using bottom-up approach"""
    cache = {0: 0}

    for i in range(1, total + 1):
        cache[i] = float('inf')
        for coin in coins:
            subproblem = i - coin

            if subproblem < 0:
                continue

            cache[i] = get_min_ignore_none(
                cache.get(i),
                cache.get(subproblem) + 1
            )

    if cache[total] == float('inf'):
        return -1

    return cache[total]
