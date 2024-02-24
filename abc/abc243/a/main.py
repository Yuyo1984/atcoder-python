import sys
from sys import stdin
input = stdin.readline

v, a, b, c = map(int, input().split())
while v >= 0:
    v -= a
    if v < 0:
        print('F')
        sys.exit()

    v -= b
    if v < 0:
        print('M')
        sys.exit()

    v -= c
    if v < 0:
        print('T')
        sys.exit()
