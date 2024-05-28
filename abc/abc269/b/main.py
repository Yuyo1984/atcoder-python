grid = []
for i in range(10):
    grid.append(list(input()))

a, b, c, d = 0, 0, 0, 0

for i in range(10):
    for j in range(10):
        if a == 0 and grid[i][j] == "#":
            a = i + 1
        if a != 0 and grid[i][j] == "#":
            b = i + 1
        if c == 0 and grid[i][j] == "#":
            c = j + 1
        if c != 0 and grid[i][j] == "#":
            d = j + 1
print(a, b)
print(c, d)
