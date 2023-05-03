#!/usr/bin/python3
"""
A method that calculates fewest number of operations to result in characthers in file

"""


def minOperations(n):
    nOpe = 0
    minOpe = 2
    while n > 1:
        while n % minOpe == 0:
            nOpe += minOpe
            n /= minOpe
        minOpe += 1
    return nOpe
