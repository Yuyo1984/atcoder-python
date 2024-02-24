from sys import stdin
input = stdin.readline

s, t, x = map(int, input().split())

if s > t:
    t += 24

if s > x:
    x += 24

if s <= x < t:
    print('Yes')
else:
    print('No')
