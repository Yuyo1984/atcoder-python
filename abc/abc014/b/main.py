n, X = map(int, input().split())
a = [*map(int, input().split())]
ans = 0

for i in range(n):
    if X & (1 << i):
        ans += a[i]
print(ans)
