from sys import stdin
input = stdin.readline

n, m, x, t, d = map(int, input().split())

if m <= x:
    print(t - (d * (x - m)))
else:
    print(t)
