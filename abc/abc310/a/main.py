from sys import stdin
input = stdin.readline

n, p, q = map(int, input().split())
D = [*map(int, input().split())]
add = q + min(D)
if p <= add:
    print(p)
else:
    print(add)

