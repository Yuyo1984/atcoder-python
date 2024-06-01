n, m, b = map(int, input().split())
a = [*map(int, input().split())]
c = [*map(int, input().split())]
ans = b * n * m + sum(a) * m + sum(c) * n

print(ans)
