import sys
input = sys.stdin.readline
import math
import numpy

N, M = map(int, input().split())
H = [0] + [*map(int, input().split())]
flag = [True] * (N+1)
for i in range(M):
    A, B = map(int, input().split())
    if H[A] < H[B]:
        flag[A] = False

print(flag.count(True))
