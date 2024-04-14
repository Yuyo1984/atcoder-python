import sys
input = sys.stdin.readline
import numpy as np
import math

def dfs(x, y, depth, energy):
    energy -= 1
    if grid[x][y] == 'G':
        return True

    e = energy_squares.get((x, y), -1)
    if energy <= e:
        energy = e

    if energy <= 0:
        return False
    grid[x][y] = '#'

    if grid[x-1][y] == '.':#左
        dfs(x-1, y, depth + 1, energy)
    if grid[x+1][y] == '.':#右
        dfs(x+1, y, depth + 1, energy)
    if grid[x][y-1] == '.':#上
        dfs(x, y-1, depth + 1, energy)
    if grid[x][y+1] == '.':#下
        dfs(x, y+1, depth + 1, energy)

    grid[x][y] = '.'


H, W = map(int, input().split())
grid = []
start = [0, 0]
for i in range(H):
    s = input()
    h = []
    for j in range(len(s)):
        h.append(s[j])
        if s[j] == 'S':
            start[0] = i
            start[1] = j
    grid.append(h)

energy = 0
energy_squares = {}
N = int(input())
for i in range(N):
    r, c, e = map(int, input().split())
    r -= 1
    c -= 1
    energy_squares[(r, c)] = e


if (dfs(start[0], start[1], 0, energy)):
    print("Yes")
else:
    print("No")
