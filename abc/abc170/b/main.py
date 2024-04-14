from sys import stdin
input = stdin.readline

X, Y = map(int, input().split())

for i in range(X):
    j = X - i
    if 2 * i + 4 * j == Y or 4 * i + 2 * j == Y:
        print("Yes")
        exit()

print("No")
