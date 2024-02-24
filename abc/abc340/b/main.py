import sys
input = sys.stdin.readline
import numpy as np

Q = int(input())
A = []
for i in range(Q):
    query = [*map(int, input().split())]
    if query[0] == 1:
        A.append(query[1])
    elif query[0] == 2:
        print(A[-query[1]])

