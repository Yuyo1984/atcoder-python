from sys import stdin
input = stdin.readline

X, Y, Z = map(int, input().split())

swap1 = 0
swap2 = 0

swap1 = X
swap2 = Y
X = swap2
Y = swap1

swap1 = X
swap2 = Z
X = swap2
Z = swap1

print(X, Y, Z)
