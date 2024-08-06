#!/usr/bin/env python3

"""
File: main.py
Description:解説AC
Author:Yuyo1984
Date: 2024-08-03
"""


# func


def main():
    # input
    N = int(input())
    S = input()

    dp = [0, 0, 0]
    r, s, p = 0, 1, 2
    # solve
    for c in S:
        dp = [max(dp[s], dp[p]), max(dp[r], dp[p]), max(dp[r], dp[s])]

        if c == "R":
            dp[s] = 0
            dp[p] += 1
        elif c == "S":
            dp[p] = 0
            dp[r] += 1
        elif c == "P":
            dp[r] = 0
            dp[s] += 1

    # output
    print(max(dp))


if __name__ == "__main__":
    main()
