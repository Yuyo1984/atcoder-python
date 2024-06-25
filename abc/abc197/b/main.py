h, w, x, y = map(int, input().split())
x -= 1
y -= 1
grid = [list(input()) for i in range(h)]

ans = 1
for d in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
    n_x = x
    n_y = y
    while True:
        n_x += d[0]
        n_y += d[1]
        if n_x < 0 or n_x >= h or n_y < 0 or n_y >= w or grid[n_x][n_y] == "#":
            break
        ans += 1

print(ans)
