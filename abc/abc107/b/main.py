h, w = map(int, input().split())
grid = []
cnt = 0
for i in range(h):
    x = list(input())
    if all(c == "." for c in x):
        cnt += 1
        continue
    grid.append(x)

h -= cnt
ans = []
skip_row = []
for j in range(w):
    if grid[0][j] == ".":
        flag = True
        for i in range(h):
            if grid[i][j] != ".":
                flag = False
                break
        if flag:
            skip_row.append(j)

for i in range(h):
    line = []
    for j in range(w):
        if j not in skip_row:
            line.append(grid[i][j])
    ans.append(line)

for x in ans:
    print("".join(x))
