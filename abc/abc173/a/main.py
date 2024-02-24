from sys import stdin
input = stdin.readline

N = int(input())

ans = (10000 - N) % 1000

print(ans)
