from sys import stdin
input = stdin.readline

n, x, t = map(int, input().split())

cnt = (n + x - 1) // x

print(t * cnt)
