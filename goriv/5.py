N = int(input())
grid = [[0 for i in range(N)] for i in range(N)]
n_x, n_y = 0, 0
grid[n_x][n_y] = 1
m_x = [-1, 0, 1, 0]
m_y = [0, 1, 0, -1]
idx = 1
for i in range(1, N * N):
    X = n_x + m_x[idx]
    Y = n_y + m_x[idx]


for i in range(N):
    print(*grid[i])
