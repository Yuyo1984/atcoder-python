import sys
input = sys.stdin.readline
import math
import numpy

N = int(input())
S = input().rstrip()

ans = 0
cnt = 0
for i in range(N-1):
    if S[i] == '>':
        cnt += 1
    else:
        ans += cnt * (cnt+1) // 2
        cnt = 0

ans += cnt * (cnt+1) // 2

print(ans)
