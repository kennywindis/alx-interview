#!/usr/bin/python3

""" A method that calculates fewest number of operations to give characthers in file """.

def minOperations(n):
    nk = 0
    mink = 2
    while n > 1:
        while n % mink == 0:
            nOpe += mink
            n /= mink
        
    return nk