H, W = map(int, input().split())
grid = [[0 for j in range(W + 1)] for i in range(H + 1)]
grid_sum = [[0 for j in range(W + 1)] for i in range(H + 1)]
for i in range(1, H + 1):
    line = [*map(int, input().split())]
    for j in range(1, W + 1):
        grid[i][j] = line[j - 1]

for i in range(1, H + 1):
    grid_sum[i][0] = grid[i][0]
    for j in range(1, W + 1):
        grid_sum[i][j] = grid_sum[i][j - 1] + grid[i][j]

for j in range(1, W + 1):
    for i in range(1, H + 1):
        grid_sum[i][j] = grid_sum[i - 1][j] + grid_sum[i][j]

Q = int(input())
for i in range(Q):
    a, b, c, d = [x for x in map(int, input().split())]
    print(
        grid_sum[c][d]
        - grid_sum[c][b - 1]
        - grid_sum[a - 1][d]
        + grid_sum[a - 1][b - 1]
    )
