import sys
input = sys.stdin.readline
import numpy as np
import math

N = int(input())
ans = 1
for i in range(10**6):
    if i**3 > N:
        break
    if str(i**3) == str(i**3)[::-1]:
        if ans < i**3:
            ans = i**3

print(ans)

