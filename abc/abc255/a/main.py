from sys import stdin
input = stdin.readline

r, c = map(int, input().split())
a = [[int(x) for x in input().split()] for i in range(2)]

print(a[r-1][c-1])
