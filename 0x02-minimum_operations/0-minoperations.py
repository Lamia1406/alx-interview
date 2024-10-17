#!/usr/bin/python3
"""
Module to calculate the minimum number of operations required to reach
exactly n characters using only "Copy All" and "Paste" operations.
"""


def minOperations(n):
    """
    The function identifies the optimal number of steps by repeatedly factoring
    the number n, since each sequence of operations (Copy All followed by
    multiple Paste operations) corresponds to multiplying the current number
    of characters.
    """
    if n <= 1:
        return 0
    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
