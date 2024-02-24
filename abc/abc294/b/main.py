from sys import stdin
input = stdin.readline

h, w = map(int, input().split())

A = []
for i in range(h):
    A.append([*map(int, input().split())])

for i in range(h):
    for j in range(w):
        if A[i][j] == 0:
            print('.', end='')
        else:
            print(chr(A[i][j] + 64), end='')
    print()