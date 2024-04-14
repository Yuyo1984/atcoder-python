import sys
input = sys.stdin.readline
import math

N = int(input())
ans = 101
length = 0.0
points = [[0, 0]]


for i in range(N):
    x, y = map(int, input().split())
    points.append([x, y])

for i in range(1, N+1):
    length = 0.0
    ans = 101
    for j in range(1, N+1):
        if i == j:
            continue
        z = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
        if length < z or (length == z and j < ans):
            ans = j
            length = z
    print(ans)

