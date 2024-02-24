from sys import stdin
input = stdin.readline

N, S, K = map(int, input().split())
P = []
Q = []
for i in range(N):
    p, q = map(int, input().split())
    P.append(p)
    Q.append(q)

ans = 0
for i in range(N):
    ans += P[i] * Q[i]

if ans < S:
    ans += K

print(ans)
