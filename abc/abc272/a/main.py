from sys import stdin
input = stdin.readline

N = int(input())
A = [*map(int, input().split())]
print(sum(A))
