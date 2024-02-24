from sys import stdin
input = stdin.readline

v, t, s, d = map(int, input().split())

print('Yes' if d / v < t or d / v > s else 'No')
