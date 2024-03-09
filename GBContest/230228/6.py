import sys
input = sys.stdin.readline
import math
import numpy

N = int(input())
A = [*map(int, input().split())]
ans = 0
for i in range(len(A)):
    x = A[i]
    while x % 2 == 0:
        x //= 2
        ans += 1

print(ans)

