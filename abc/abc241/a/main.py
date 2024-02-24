from sys import stdin
input = stdin.readline

a = [*map(int, input().split())]

ans = 0
push = 0
for i in range(3):
    push = a[push]

print(push)
