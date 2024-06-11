n, k = map(int, input().split())
l = [*map(int, input().split())]
l.sort(reverse=True)

ans = sum(l[0:k])
print(ans)
