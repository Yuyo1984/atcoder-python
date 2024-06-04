N, S = map(int, input().split())
A = [0 for i in range(69)]
x = [*map(int, input().split())]
for i, a in enumerate(x, start=1):
    A[i] = a

dp = [[False for _ in range(10009)] for _ in range(69)]
dp[0][0] = True

for i in range(1, S + 1):
    dp[0][i] = False

for i in range(1, N + 1):
    for j in range(S + 1):
        if j < A[i]:
            if dp[i - 1][j]:
                dp[i][j] = True
            else:
                dp[i][j] = False
        elif j >= A[i]:
            if dp[i - 1][j] or dp[i - 1][j - A[i]]:
                dp[i][j] = True
            else:
                dp[i][j] = False

if dp[N][S]:
    print("Yes")
else:
    print("No")
