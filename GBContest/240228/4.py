import sys
input = sys.stdin.readline
import math
import numpy

N, X = map(int, input().split())
S = input().rstrip()
ans = X
for i in range(len(S)):
    if S[i] == 'o':
        ans += 1
    else:
        if ans >= 1:
            ans -= 1

print(ans)

