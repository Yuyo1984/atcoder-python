N = int(input())
A = [*map(int, input().split())]

ans = 0
for i in range(1, N+1):
    ans += A[i-1] * (-N+2*i-1)

print(ans)
