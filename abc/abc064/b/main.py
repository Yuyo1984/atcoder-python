N = int(input())
a = [*map(int, input().split())]

a.sort(reverse=True)
ans = 0
for i in range(N - 1):
    ans += a[i] - a[i + 1]
print(ans)
