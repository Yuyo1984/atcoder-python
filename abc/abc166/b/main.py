from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
ansl = [[True] * (n+1)]
ans = 0

for i in range(k):
    x = int(input())
    list = [*map(int, input().split())]
    for j in range(x):
        m = list[j]
        ansl[0][m] = False

for i in range(1, n+1):
    if ansl[0][i] == True:
        ans += 1

print(ans)
