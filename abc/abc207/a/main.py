from sys import stdin
input = stdin.readline

a, b, c = map(int, input().split())

print(max(a+b, a+c, b+c))
