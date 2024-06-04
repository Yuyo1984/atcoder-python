n, w = map(int, input().split())
a = [*map(int, input().split())]
weights = set()
ans = 0

for i in a:
    weights.add(i)

for i in range(n):
    for j in range(i + 1, n):
        sum_w = a[i] + a[j]
        weights.add(sum_w)

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            sum_w = a[i] + a[j] + a[k]
            weights.add(sum_w)

for i in weights:
    if i <= w:
        ans += 1

print(ans)
