from sys import stdin
input = stdin.readline

n, p, q, r, s = map(int, input().split())
A = [*map(int, input().split())]

A[p-1:q], A[r-1:s] = A[r-1:s], A[p-1:q]
print(*A)
