from sys import stdin
input = stdin.readline

N, X = map(int, input().split())
A = [*map(int, input().split())]
flag = [False] * N
known = X - 1
for i in range(N):
    if flag[known] == False:
        flag[known] = True
    known = A[known] - 1

print(flag.count(True))

