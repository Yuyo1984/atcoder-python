from math import sqrt

N, K = map(int, input().split())
A = [*map(int, input().split())]
A = [x - 1 for x in A]
p = [[*map(int, input().split())] for i in range(N)]

result = 0
for i in range(N):
    d = float("inf")
    for x in A:
        d = min(d, (p[i][0] - p[x][0]) ** 2 + (p[i][1] - p[x][1]) ** 2)
    result = max(result, d)

print(sqrt(result))
