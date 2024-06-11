N = int(input())
grid = []
for i in range(N):
    grid.append(list(input()))

new_grid = [["" for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        if i == 0 and 1 <= j < N:
            new_grid[i][j] = grid[i][j - 1]
        elif 1 <= i < N and j == N - 1:
            new_grid[i][j] = grid[i - 1][j]
        elif i == N - 1 and 0 <= j < N - 1:
            new_grid[i][j] = grid[i][j + 1]
        elif 0 <= i < N - 1 and j == 0:
            new_grid[i][j] = grid[i + 1][j]
        else:
            new_grid[i][j] = grid[i][j]
for i in range(N):
    print("".join(new_grid[i]))
