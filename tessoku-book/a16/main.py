N = int(input())
A = [0 for i in range(100010)]
B = [0 for i in range(100010)]
a = [*map(int, input().split())]
for i, x in enumerate(a, start=2):
    A[i] = x
b = [*map(int, input().split())]
for i, x in enumerate(b, start=3):
    B[i] = x

dp = [0 for i in range(100010)]
dp[1] = 0
dp[2] = A[2]
for i in range(3, N + 1):
    dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + B[i])

print(dp[N])
