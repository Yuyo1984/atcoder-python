from sys import stdin
input = stdin.readline

a, b = map(int, input().split())
print("{:0.3f}".format(b / a))
