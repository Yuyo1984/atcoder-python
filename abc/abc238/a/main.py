from sys import stdin
input = stdin.readline

n = int(input())

if n == 1 or n >= 5:
    print('Yes')
else:
    print('No')
