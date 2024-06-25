import bisect

N, Q = map(int, input().split())
A = [*map(int, input().split())]

A.sort()

for i in range(Q):
    x = int(input())
    print(N - bisect.bisect_left(A, x))
