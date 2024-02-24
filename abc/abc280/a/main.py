from sys import stdin
input = stdin.readline

H, W = map(int, input().split())
ans = 0
for i in range(H):
    ans += input().count('#')

print(ans)

