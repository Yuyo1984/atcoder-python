import sys
input = sys.stdin.readline
import numpy as np

N = int(input())
A = [*map(int, input().split())]
cnt = 0
for i in range(len(A)):
    cnt += A[i]
    if cnt < 0:
        cnt = 0

print(cnt)

