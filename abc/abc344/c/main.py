import sys
input = sys.stdin.readline
import numpy as np
import math

N = int(input())
A = [*map(int, input().split())]
M = int(input())
B = [*map(int, input().split())]
L = int(input())
C = [*map(int, input().split())]
Q = int(input())
X = [*map(int, input().split())]
num_set = set()
for i in range(N):
    for j in range(M):
        for k in range(L):
            sum_nums = A[i] + B[j] + C[k]
            num_set.add(sum_nums)

for i in X:
    if i in num_set:
        print("Yes")
    else:
        print("No")

