h, w, n = map(int, input().split())
grid = [["." for i in range(w)] for j in range(h)]

n_x, n_y = 0, 0
direction = ["U", "R", "D", "L"]
d_n = 0
n_d = direction[d_n]


for i in range(n):
    if grid[n_x][n_y] == ".":
        grid[n_x][n_y] = "#"
        d_n += 1
        d_n %= 4
        n_d = direction[d_n]

    else:
        grid[n_x][n_y] = "."
        d_n += 3
        d_n %= 4
        n_d = direction[d_n]

    if n_d == "U":
        n_x -= 1
    elif n_d == "R":
        n_y += 1
    elif n_d == "D":
        n_x += 1
    elif n_d == "L":
        n_y -= 1
    if n_x == -1:
        n_x = h - 1
    if n_y == -1:
        n_y = w - 1
    if n_x == h:
        n_x = 0
    if n_y == w:
        n_y = 0

# print(n_x, n_y)
for i in range(h):
    print("".join(grid[i]))
