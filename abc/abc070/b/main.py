a, b, c, d = map(int, input().split())

l = max(a, c)
r = min(b, d)
ans = max(0, r - l)
print(ans)
