import sys
input = sys.stdin.readline
import math
import numpy


H, W = map(int, input().split())
grid = []
for i in range(H):
    grid.append(list(input().rstrip()))

ans = [[0 for i in range(W)] for j in range(H)]
for i in range(H):
    for j in range(W):
        for k in range(-1, 1):
            for l in range(-1, 1):
                x = i + k
                y = j + l
                if x < 0 or y < 0 or x >= H or y >= W:
                    break
                else:
                    if grid[x][y] == '#':
                        ans[x][y] += 1

