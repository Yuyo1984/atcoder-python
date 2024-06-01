N = int(input())
h = [0] + [*map(int, input().split())]
dp = [0 for i in range(100010)]

dp[1] = 0
dp[2] = abs(h[2] - h[1])

for i in range(3, N + 1):
    dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]), dp[i - 2] + abs(h[i] - h[i - 2]))

print(dp[N])
