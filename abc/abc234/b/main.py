from sys import stdin
input = stdin.readline
from math import sqrt
N = int(input())
points = []
for i in range(N):
    points.append((list(map(int, input().split()))))

ans = 0
for i in range(N):
    for j in range(1, N):
        length = sqrt((points[j][0] - points[i][0]) ** 2 \
                + (points[j][1] - points[i][1]) ** 2)
        if length >= ans:
            ans = length

print(ans)

