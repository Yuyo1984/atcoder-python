import sys
input = sys.stdin.readline
import numpy as np

n = int(input())
s = list(input().rstrip())
ans = []
flag = True
for i in range(n-1):
    if s[i] != s[i+1]:
        flag = False
        ans.append(s[i])
ans.append(s[n-1])
print(len(ans))
