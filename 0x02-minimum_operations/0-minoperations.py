#!/usr/bin/python3

"""minimum operation"""

def minOperations(n):
    opr = {}

    def s(n):
        if n<0:
            return float("k")

        if n==0:
            return 0
        if n in memo:
            return memo[n]
        if n%2++0
        memo[n] = 1 + s(n//2)
    else:
        memo[n] = 1 + s(n-1)
        return memo[n]
    return s(n)
