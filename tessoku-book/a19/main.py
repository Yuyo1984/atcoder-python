N, W = map(int, input().split())
imp = -(10**10)
dp = [[imp for _ in range(100009)] for _ in range(109)]
dp[0][0] = 0
w = [imp]
v = [imp]
for i in range(N):
    x, y = map(int, input().split())
    w.append(x)
    v.append(y)

for i in range(1, N + 1):
    for j in range(W + 1):
        if j < w[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])

ans = 0
for i in range(W + 1):
    ans = max(ans, dp[N][i])
print(ans)
