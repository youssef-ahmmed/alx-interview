#!/usr/bin/python3
"""Min Operations Algorithm"""
import math


def minOperations(n):
    """function to find the min operation to print exactly n's 'H' in a file"""
    if n <= 1:
        return 0

    prime_factors = []

    while n % 2 == 0:
        prime_factors.append(2)
        n = n // 2

    for i in range(3, int(math.sqrt(n) + 1), 2):

        while n % i == 0:
            prime_factors.append(i)
            n = n // i

    if n > 2:
        prime_factors.append(n)

    return sum(prime_factors)
