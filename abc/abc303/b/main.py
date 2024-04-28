import math
N, M = map(int, input().split())
A = []
for i in range(M):
    A.append([*map(int, input().split())])

pair = set()
for i in range(M):
    for j in range(1, N):
        pair.add((min(A[i][j-1], A[i][j]), max(A[i][j-1], A[i][j])))

print(N * (N-1) // 2 - len(pair))


