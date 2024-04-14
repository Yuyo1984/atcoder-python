from sys import stdin
input = stdin.readline

N, M, T = map(int, input().split())
full = N
C = 0
flag = True
for i in range(M):
    A, B = map(int, input().split())
    N -= A - C
    if N <= 0:
        flag = False
        break
    if N < full:
        N = min(N - B + A, full)
    C = B
    if i == M - 1:
        N -= T - C
    if N <= 0:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
