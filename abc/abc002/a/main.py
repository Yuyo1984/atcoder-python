from sys import stdin
input = stdin.readline

x, y = map(int, input().split())
if x > y:
    print(x)
else:
    print(y)
