#!/usr/bin/env python3

"""
File: main.py
Description:
Author:Yuyo1984
Date: 2024-08-03
"""

# func


def main():
    # input
    n, m = map(int, input().split())
    A = [*map(int, input().split())]
    # solve
    A = sorted(A)
    ans = 0
    le = 0
    ri = 10**18 + 1
    while ri - le > 1:
        mid = (le + ri) // 2
        s_now = sum(min(a, mid) for a in A)
        if s_now <= m:
            le = mid
        else:
            ri = mid

    # output
    print(le if le < 10**18 else "infinite")


if __name__ == "__main__":
    main()
