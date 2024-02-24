from sys import stdin
input = stdin.readline

x, y = map(int, input().split())

if x >= y:
    print(0)
else:
    ans = 0
    while x < y:
        ans += 1
        x += 10
    print(ans)
