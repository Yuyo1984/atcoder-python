n, s = map(int, input().split())
A = [*map(int, input().split())]

dp = [[None] * (s+1) for i in range(n+1)]
dp[0][0] = True
for i in range(1, s+1):
    dp[0][i] = False

for i in range(1, n+1):
    for j in range(0, s+1):
        if j < A[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            if (dp[i-1][j] == True or dp[i-1][j-A[i-1]] == True):
                dp[i][j] = True
            else:
                dp[i][j] = False

if dp[n][s] == True:
    print("Yes")
else:
    print("No")

