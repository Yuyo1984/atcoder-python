from sys import stdin
input = stdin.readline

N, W = map(int, input().split())

print(N // W)
