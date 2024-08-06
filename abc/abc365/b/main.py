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
    n = int(input())
    A = [*map(int, input().split())]
    sortA = sorted(A)
    # solve
    x = sortA[-2]
    # output
    for i, v in enumerate(A, start=1):
        if v == x:
            print(i)
            exit()


if __name__ == "__main__":
    main()
