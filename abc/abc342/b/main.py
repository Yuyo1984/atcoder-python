import sys
input = sys.stdin.readline
import numpy as np

N = int(input())
P = [*map(int, input().split())]
Q = int(input())
for i in range(Q):
    A, B = map(int, input().split())
    x = P.index(A)
    y = P.index(B)
    if x < y:
        print(A)
    else:
        print(B)

