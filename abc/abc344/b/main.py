import sys
input = sys.stdin.readline
import numpy as np
import math

A = []
while True:
    x = input().rstrip()
    if x == "":
        break
    else:
        A.append(x)

for i in range(len(A)-1, -1, -1):
    print(A[i])

