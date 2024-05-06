h, w = map(int, input().split())
grid = []
for i in range(h):
    grid.append(list(map(int, input().split())))

for i in range(h-1):
    for j in range(i, h):
        for k in range(w-1):
            for l in range(k, w):
                if grid[i][k] + grid[j][l] > grid[j][k] + grid[i][l]:
                    print("No")
                    exit()

print("Yes")
