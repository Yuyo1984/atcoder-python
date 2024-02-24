from sys import stdin
input = stdin.readline

N, H, X = map(int, input().split())
P = [*map(int, input().split())]
ans = 0
for i in range(N):
    if P[i] + H >= X:
        ans = i
        break

print(i+1)

