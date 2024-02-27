N = int(input())
A = [*map(int, input().split())]

ans = 0
for i in range(N):
    ans += A[i]

print(ans % 100)
