import sys
input = sys.stdin.readline
import math
import numpy

N, M = map(int, input().split())
AB = []
for i in range(M):
    AB.append([*map(int, input().split())])

for i in range(1, M+1):
    ans = []
    d = 0
    chain = [0] * (N+1)
    for j in range(M):
        if AB[M][0] == i:
            chain[AB[M][1]] = 1
            d += 1
    ans.append(d)
    for i in range(1, len(chain)+1):
        if chain[i] == 1:
            ans.append(i)
    print(*ans)


