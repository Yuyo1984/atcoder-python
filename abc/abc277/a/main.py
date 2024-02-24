from sys import stdin
input = stdin.readline

N, X = map(int, input().split())
P = [*map(int, input().split())]
for i in P:
    if i == X:
        print(P.index(i)+1)
        break

