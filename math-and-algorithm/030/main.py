N, W = map(int, input().split())
w_l = [0]
v_l = [0]
for i in range(N):
    w, v = map(int, input().split())
    w_l.append(w)
    v_l.append(v)

dp = [[None for i in range(W+1)] for j in range(N+1)]
dp[0][0] = 0
for i in range(1, W+1):
    dp[0][i] = -1<<60

for i in range(1, N+1):
    for j in range(W+1):
        if j < w_l[i]:
            dp[i][j] = dp[i-1][j]
        if j >= w_l[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w_l[i]] + v_l[i])

ans = 0
for i in range(W+1):
    ans = max(ans, dp[N][i])
print(ans)

