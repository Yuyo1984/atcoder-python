import sys
input = sys.stdin.readline
import numpy as np
import math

N = int(input())
A = [*map(int, input().split())]
ansl = []
for i in range(N-1):
    ansl.append(A[i] * A[i+1])

print(*ansl)
