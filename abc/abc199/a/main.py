from sys import stdin
input = stdin.readline

a, b, c = map(int, input().split())

if a**2 + b**2 < c**2:
    print('Yes')
else:
    print('No')
