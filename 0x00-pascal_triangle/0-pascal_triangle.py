#!/usr/bin/python3
'''Module to return pascal triangle'''


def solve(k):
   for k in range(k+1):
      for d in range(k-i):
         print(' ', end='')

      C = 1
      for j in range(1, i+1):
         print(C, ' ', sep='', end='')
         C = C * (i - j) // j
      print()

k = 5
solve(k)
