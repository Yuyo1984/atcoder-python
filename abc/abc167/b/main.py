from sys import stdin
input = stdin.readline

A, B, C, K = map(int, input().split())

ans = 0
ans += min(A, K)
K -= A
K -= min(B, K)
ans -= min(C, K)

print(ans)

