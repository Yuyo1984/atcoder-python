N = int(input())
h = [0] + [*map(int, input().split())]
dp = [0] * (N+1)
for i in range(1, N+1):
    if i == 1:
        dp[i] = 0
    elif i == 2:
        dp[i] = abs(h[i-1] -h[i])
    elif i >= 3:
        v1 = dp[i-1] + abs(h[i-1] - h[i])
        v2 = dp[i-2] + abs(h[i-2] - h[i])
        dp[i] = min(v1, v2)

print(dp[N])

