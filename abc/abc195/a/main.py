from sys import stdin
input = stdin.readline

m, h = map(int, input().split())

if h % m == 0:
    print('Yes')
else:
    print('No')
