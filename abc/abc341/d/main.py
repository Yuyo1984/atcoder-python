import sys
input = sys.stdin.readline
import numpy as np

N, M, K = map(int, input().split())
if N < M:
    N, M = M, N
X = N * M
ans = X * (K % M) + N
print(ans)
