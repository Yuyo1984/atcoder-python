import sys
input = sys.stdin.readline
import math
import numpy

N, Q = map(int, input().split())
ans = [0] * (N+1)
for i in range(Q):
    L, R, T = map(int, input().split())
    ans[L:R+1] = [T] * (R-L+1)

for i in range(1, N+1):
    print(ans[i])

