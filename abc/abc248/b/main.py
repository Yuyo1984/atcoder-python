a, b, k = map(int, input().split())

ans = 0
cnt = a
while cnt < b:
    ans += 1
    cnt *= k

print(ans)
