import sys
input = sys.stdin.readline

grid = []

for i in range(4):
    grid.append(list(input().rstrip().split()))

for i in range(3, -1, -1):
    for j in range(3, -1, -1):
        if j == 0:
            print(grid[i][j], end='')
        else:
            print(grid[i][j], end=' ')
    print()
