#!/usr/bin/python3



"""
Method  that calculates fewest number of operations

"""


def minOperations(n):
    nk = 0
    mink = 2
    while n > 1:
        while n % mink == 0:
            nk += mink
            n /= mink
        mink += 1
    return nk
