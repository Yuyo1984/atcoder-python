from sys import stdin
input = stdin.readline

N = int(input())
S = []
A = []
for i in range(N):
    s, a = map(str, input().split())
    S.append(s)
    A.append(int(a))

x = A.index(min(A))

cnt = 0
while cnt < N:
    print(S[x])
    x += 1
    x %= N
    cnt += 1

