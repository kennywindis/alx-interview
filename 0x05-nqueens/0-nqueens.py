#!/usr/bin/env python3
"""A program that solves the N queens problem,
Usage: nqueens N,
where N must be an integer greater or equal to 4"""

import sys


def nqueens(n: int):
    """
    backtracking
    """
    matrix = [[0 for k in range(n)] for d in range(n)]
    print(str(matrix))


if __name__ == "__main__":
    if len(sys.argv) > 2 or len(sys.argv) < 2:
        print("Usage: nqueens N")
        exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)

    nqueens(int(sys.argv[1]))
