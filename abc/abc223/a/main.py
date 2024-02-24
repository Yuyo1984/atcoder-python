from sys import stdin
input = stdin.readline

x = int(input())

if x % 100 == 0 and x >= 100:
    print('Yes')
else:
    print('No')
