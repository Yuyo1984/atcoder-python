N = int(input())
A = [0] + [*map(int, input().split())]
B = [0] + [*map(int, input().split())]
C = [0] + [*map(int, input().split())]

ans = B[A[1]]
for i in range(2, N+1):
    ans += B[A[i]]
    if A[i-1] == A[i]-1:
        ans += C[A[i-1]]

print(ans)

