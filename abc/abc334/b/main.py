from sys import stdin
input = stdin.readline

A, M, L, R = map(int, input().split())

ans = 0
if L != R:
    ans = (R - L) // M + 1
if (R - L) % M == 0:
    ans -= 1
if L == R:
    ans = 0
print(ans)

