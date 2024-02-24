from sys import stdin
input = stdin.readline

N, L = map(int, input().split())
A = [*map(int, input().split())]

ans = 0
for i in A:
    if i >= L:
        ans += 1

print(ans)

