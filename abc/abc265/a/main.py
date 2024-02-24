from sys import stdin
input = stdin.readline

x, y, n = map(int, input().split())
ans = x * n
for i in range(1, (n//3)+1):
    price = y * i + x * (n-i*3)
    if price <= ans:
        ans = price

print(ans)

