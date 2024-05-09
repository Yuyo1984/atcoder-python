def rotate(grid):
    grid = grid[::-1]
    grid = list(map(list, zip(*grid)))
    return grid

n = int(input())
a = []
for i in range(n):
    a.append([*map(int, input().split())])
b = []
for i in range(n):
    b.append([*map(int, input().split())])

for i in range(4):
    a = rotate(a)
    flag = True
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1 and b[i][j] != 1:
                flag = False
    if flag:
        print("Yes")
        exit()

print("No")
