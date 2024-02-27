N = int(input())
A = [*map(int, input().split())]
B = [*map(int, input().split())]

a = 0.0
b = 0.0
for i in range(N):
    a += A[i]
    b += B[i]

ans = a / 3 + (b * 2) / 3
print(ans)

