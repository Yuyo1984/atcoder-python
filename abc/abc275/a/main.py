from sys import stdin
input = stdin.readline

N = int(input())
H = [*map(int, input().split())]
print(H.index(max(H)) + 1)
