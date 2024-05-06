h, w = map(int, input().split())
grid = []
for i in range(h):
    grid.append(list(input()))

box_h = []
box_w = []
for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            box_h.append(i)
            box_w.append(j)

a = min(box_h)
b = max(box_h)
c = min(box_w)
d = max(box_w)

for i in range(a, b+1):
    for j in range(c, d+1):
        if grid[i][j] == '.':
            print(i+1, j+1)
            exit()

