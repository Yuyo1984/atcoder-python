from sys import stdin
input = stdin.readline

N, A, B = map(int, input().split())
C = [*map(int, input().split())]

X = A + B
print(C.index(X)+1)
