from sys import stdin
input = stdin.readline

N, X = map(int, input().split())
S = [*map(int, input().split())]

ans = 0
for i in S:
    if i <= X:
        ans += i

print(ans)

