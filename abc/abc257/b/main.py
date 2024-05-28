N, K, Q = map(int, input().split())
A = [*map(int, input().split())]
L = [*map(int, input().split())]

for i in range(Q):
    x = L[i]
    now = A[x - 1]
    next = now + 1
    if now != N and next not in A:
        A[x - 1] += 1

print(*A)
