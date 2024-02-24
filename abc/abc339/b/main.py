import sys
input = sys.stdin.readline
import numpy as np

H, W, N = map(int, input().split())
grid = []
for _ in range(H):
    a = ['.'] * W
    grid.append(a)
x, y = 0, 0
p_d = 'U'
flag = True
for i in range(N):
    if grid[x][y] == '.':
        grid[x][y] = '#'
        flag = False
    else:
        grid[x][y] = '.'
        flag = True
    if flag:
        if p_d == 'U':
            p_d = 'L'
            y -= 1
        elif p_d == 'R':
            p_d = 'U'
            x -= 1
        elif p_d == 'D':
            p_d = 'R'
            y += 1
        elif p_d == 'L':
            p_d = 'D'
            x += 1
    else:
        if p_d == 'U':
            p_d = 'R'
            y += 1
        elif p_d == 'R':
            p_d = 'D'
            x += 1
        elif p_d == 'D':
            p_d = 'L'
            y -= 1
        elif p_d == 'L':
            p_d = 'U'
            x -= 1
    if x >= H:
        x = 0
    if y >= W:
        y = 0
    if x < 0:
        x = H - 1
    if y < 0:
        y = W - 1

for i in range(H):
    print("".join(grid[i]))
