import sys
input = sys.stdin.readline
import math
import numpy

N = int(input())
A = [*map(int, input().split())]

ans = 0
x = 0
y = 0
for i in range(0, N):
    if (i+1) == A[i]:
        x += 1
    else:
        if A[A[i]-1] == i+1:
            y += 1

print(math.comb(x, 2) + y//2)

