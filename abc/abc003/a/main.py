from sys import stdin
input = stdin.readline

N = int(input())
l = [i for i in range(1, N+1)]
ans = sum(l) * 10000 / N
print(ans)
