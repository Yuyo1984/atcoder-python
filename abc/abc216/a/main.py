from sys import stdin
input = stdin.readline

x, y = map(int, input().split('.'))

print(str(x) + '-' if 0 <= y <= 2 else x if 3 <= y <= 6 else str(x) + '+')
