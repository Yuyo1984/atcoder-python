from sys import stdin
input = stdin.readline

n = int(input())
A = [*map(int, input().split())]

for i in A:
    if i % 2 == 0:
        print(i, end = ' ')
