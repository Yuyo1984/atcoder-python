import sys
input = sys.stdin.readline
import math
import numpy

N = int(input())
V = [*map(int, input().split())]
C = [*map(int, input().split())]

ans = 0
for i in range(N):
    x = V[i]
    y = C[i]
    if x - y > 0:
        ans += x - y 

print(ans)

