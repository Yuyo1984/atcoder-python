from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
A = [*map(int, input().split())]
for i in range(K):
    del A[0]
    A.append(0)

print(*A)
