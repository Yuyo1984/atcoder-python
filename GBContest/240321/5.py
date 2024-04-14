import sys
input = sys.stdin.readline
import math
import numpy

L, H = map(int, input().split())
N = int(input())
for i in range(N):
    x = int(input())
    if L <= x <= H:
        print(0)
    elif x < L:
        print(L - x)
    else:
        print(-1)

