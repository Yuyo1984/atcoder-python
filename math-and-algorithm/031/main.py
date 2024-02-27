N = int(input())
A = [*map(int, input().split())]

dp =[[0 for i in range(500001)] for i in range(2)]

for i in range(1, N+1):
    dp[0][i] = max(dp[0][i-1], dp[1][i-1])

    dp[1][i] = dp[0][i-1] + A[i-1]

print(max(max(dp[0]), max(dp[1])))

