N = int(input())
K = int(input())
x = [*map(int, input().split())]

ans = 0

for i in range(N):
    d1 = 2 * x[i]
    d2 = 2 * abs(x[i] - K)
    if d1 <= d2:
        ans += d1
    else:
        ans += d2
print(ans)
