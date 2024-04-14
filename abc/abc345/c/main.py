import sys
input = sys.stdin.readline
import numpy as np
import math

S = input().rstrip()
cnt = [0] * 26
same = False
n = len(S)
for i in range(n):
    cnt[ord(S[i]) - ord('a')] += 1

ans = n * n
for i in range(26):
    ans -= (cnt[i]) ** 2
    if cnt[i] > 1:
        same = True

ans //= 2
if same:
    ans += 1
print(ans)

