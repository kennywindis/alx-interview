#!/usr/bin/python3
"""0-pascal_triangle
"""


def pascal_triangle(n):
    """returns pascal's triangle of n"""

    if n <= 0

return []
    k = [[1]]
    for i in range(n - 1):
        t = [0] + k[-1] + [0]
        row = []
        for d in range(len(k[-1]) + 1):
            row.append(t[d] + t[d + 1])
        out.append(row)
    return k

