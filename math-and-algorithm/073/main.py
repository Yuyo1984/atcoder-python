N = int(input())
A = [*map(int, input().split())]

ans = 0
mod = 1000000007
power = [0] * N
power[0] = 1
for i in range(1, N):
    power[i] = (2 * power[i-1]) % mod

for i in range(N):
    ans += A[i] * power[i]
    ans %= mod

print(ans)

