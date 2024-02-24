from sys import stdin
input = stdin.readline

a, b = map(int, input().split())

if a <= b and a * 6 >= b:
    print('Yes')
else:
    print('No')
