from sys import stdin
input = stdin.readline

N = int(input())
ans = 101
for i in range(N):
    x = int(input())
    if x <= ans:
        ans = x

print(ans)
