import sys
input = sys.stdin.readline
import numpy as np

H, W, N = map(int, input().split())
T = input().rstrip()
grid = [[] for i in range(H)]
for i in range(H):
    line = list(input().rstrip())
    for j in range(len(line)):
        if line[j] == '#':
            grid[i].append(False)
        else:
            grid[i].append(True)

move = {L:[0, -1], U:[-1, 0], D:[1, 0], R:[0, 1]}
for i in range(1, H-1):
    for j in range(1, W-1):
        for k in range(T):
            if A[]
print(grid)


