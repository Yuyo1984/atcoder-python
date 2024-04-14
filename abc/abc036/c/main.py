from sys import stdin
input = stdin.readline

N = int(input())
A = []
for i in range(N):
    A.append(int(input()))

S = sorted(list(set(A)))
b = {x:i for i, x in enumerate(S)}
B = []
for a in A:
    B.append(b[a])

for x in B:
    print(x)
