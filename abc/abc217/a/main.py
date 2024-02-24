from sys import stdin
input = stdin.readline

s, t = map(str, input().split())

if s <= t:
    print('Yes')
else:
    print('No')
