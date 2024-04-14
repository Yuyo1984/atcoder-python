from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
p = [*map(int, input().split())]

p.sort()

ans = sum(p[0:K])
print(ans)
