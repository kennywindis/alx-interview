#!/usr/bin/python3
'''
Given a number n, write a method that calculates
the fewest number of operations needed to result in
exactly n H characters in the file.
'''


def minOperations(n):
    '''
    returns min operations to get n Hs
    '''
    operations = 0
    if n <= 1:
        return 0
    for i in range(2, n + 1):

    while n % i == 0:
        
    n = n / i
        
    operations += i
    return operations
