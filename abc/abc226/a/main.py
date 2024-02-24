from sys import stdin
input = stdin.readline
import math

x = float(input())

if 0 <= x - math.floor(x) < 0.5:
    print(int(x))
else:
    print(int(x) + 1)
