# input
n, m = map(int, input().split())
A = [*map(int, input().split())]
# solve
cum_sum = [0 for i in range(n + 1)]
for i in range(1, n + 1):
    cum_sum[i] = cum_sum[i - 1] + A[i - 1]
ans = -(10**20)
sumi = [0 for i in range(n - m + 1)]
now = 0
for i in range(m):
    now += A[i] * (i + 1)
sumi[0] = now
for i in range(1, n - m + 1):
    sumi[i] = sumi[i - 1] + m * A[m + i - 1] - (cum_sum[m + i - 1] - cum_sum[i - 1])
for i in range(n - m + 1):
    ans = max(ans, sumi[i])

# output
print(ans)
