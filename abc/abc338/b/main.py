import sys
input = sys.stdin.readline
import numpy as np

s = input().rstrip()
ans = 'z'
cnt = 0
for i in s:
    if cnt < s.count(i) or (cnt == s.count(i) and ans > i):
        ans = i
        cnt = s.count(i)

print(ans)
