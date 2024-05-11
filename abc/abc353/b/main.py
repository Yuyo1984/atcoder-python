#input
n, k = map(int, input().split())
a = [*map(int, input().split())]
#solve
empty = k
ans = 0
i = 0
while i != n:
    if empty < a[i]:
        empty = k
        ans += 1
    else:
        empty -= a[i]
        i += 1

ans += 1
#output
print(ans)
