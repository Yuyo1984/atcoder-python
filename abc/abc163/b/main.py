from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
A = [*map(int, input().split())]

x = sum(A)

if x <= N:
    print(N - x)
else:
    print(-1)

