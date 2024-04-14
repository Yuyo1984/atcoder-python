from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
S = input().rstrip()
T = input().rstrip()

ans = 3
if T[M-N:] == S:
    ans -= 1
if T[0:N] == S:
    ans -= 2

print(ans)
