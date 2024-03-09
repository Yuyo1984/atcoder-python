import sys
input = sys.stdin.readline
import math
import numpy

N = int(input())
A = [*map(int, input().split())]

B = sorted(A)
print(B)
ansl = []

for n in range(N):
    li = [i for i, x in enumerate(B) if x == A[n]]
    print(li)
    ansl.append(sum(B[max(li)+1:]))
    print(ansl)
print(*ansl)
