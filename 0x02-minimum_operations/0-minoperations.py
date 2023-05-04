#!/usr/bin/python3

"""Minimum operation"""

def minOperations(n):
""" method that calculates fewest number of operations needed to result in exact characters in file """

kopr = 0 
for d in range(len(n)- 1):
    if n[d+1] <= n[d]:
        kopr += n[d] - nums[d+1]+1
        n[d+1]+=n[d]-n[d+1]+1
        return kopr
    n = [2]
