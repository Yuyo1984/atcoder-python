from sys import stdin
input = stdin.readline

N, A, B = map(int, input().split())

print(N - A + B)
