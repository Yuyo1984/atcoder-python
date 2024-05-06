
h, w = map(int, input().split())
grid = []
for i in range(h):
    grid.append(list(map(int,input().split())))

m = 101
for i in range(h):
    for j in range(w):
        if grid[i][j] < m:
            m = grid[i][j]

ans = 0
for i in range(h):
    for j in range(w):
        ans += grid[i][j] - m

print(ans)

