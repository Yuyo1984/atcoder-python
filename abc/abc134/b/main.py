n, d = map(int, input().split())

ans = 0
while n > 0:
    ans += 1
    n = n - (2*d+1)

print(ans)
