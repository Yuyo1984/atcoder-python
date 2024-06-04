N, Q = map(int, input().split())
A = [0] * 100009
B = [0] * 100009
L = [0] * 100009
R = [0] * 100009

x = [*map(int, input().split())]
for i, a in enumerate(x, start=1):
    A[i] = a
for j in range(1, Q + 1):
    x, y = map(int, input().split())
    L[j] = x
    R[j] = y
for i in range(1, N + 1):
    B[i] = B[i - 1] + A[i]

for j in range(1, Q + 1):
    print(B[R[j]] - B[L[j] - 1])
