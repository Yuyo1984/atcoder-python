N = int(input())
A = [*map(int, input().split())]

ans = 0
h = A[0]

for i in range(1, N):
    if A[i] < h:
        ans += abs(A[i] - h)
    else:
        h = A[i]

print(ans)
