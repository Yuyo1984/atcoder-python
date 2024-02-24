from sys import stdin
input = stdin.readline

M, D = map(int, input().split())
y, m, d = map(int, input().split())

d = d + 1
if d > D:
    d -= D
    m += 1
    if m > M:
        m -= M
        y += 1

print(y, m, d)

