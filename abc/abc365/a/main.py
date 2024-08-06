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
    # solve
    if n % 4 != 0:
        print(365)
    elif n % 4 == 0 and n % 100 != 0:
        print(366)
    elif n % 100 == 0 and n % 400 != 0:
        print(365)
    elif n % 400 == 0:
        print(366)
    # output


if __name__ == "__main__":
    main()
