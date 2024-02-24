import sys
input = sys.stdin.readline
import numpy as np

n = int(input())
A = [*map(int, input().split())]
ansm = {}
ansl = []
for i in range(n):
    ansm[A[i]] = i+1
ansl.append(ansm[-1])
x = ansl[-1]

for i in range(n-1):
    ansl.append(ansm[x])
    x = ansm[x]

print(*ansl)
