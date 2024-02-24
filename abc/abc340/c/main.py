import sys
input = sys.stdin.readline
import math
import numpy as np

N = int(input())
cnt1, cnt2 = 0, 0
M = N
while M >= 2:
    cnt1 += 1
    if M % 2 == 1:
        cnt2 += 2 ** (cnt1-1)
    M //= 2
ans = N * cnt1 + 2 * cnt2

print(ans)
