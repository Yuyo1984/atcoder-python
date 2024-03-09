import sys
input = sys.stdin.readline
import numpy as np
import math

N = int(input())
A = []
for i in range(N):
    A.append([*map(int, input().split())])

for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            print(j+1, end=" ")
    print()

