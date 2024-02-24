from sys import stdin
input = stdin.readline

N = int(input())
P = [*map(int, input().split())]
P[0] -= 1
ans = 0
for i in range(1, N):
    diff = P[i] - P[0]
    if ans <= diff:
        ans = diff

print(ans)
