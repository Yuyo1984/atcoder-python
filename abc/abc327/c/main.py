from sys import stdin
input = stdin.readline

grid = []
for i in range(9):
    grid.append([*map(int,input().split())])

one_to_nine = [i for i in range(1, 10)]

for i in range(9):
    x = sorted(grid[i])
    if x != one_to_nine:
        print("No")
        exit()

for i in range(9):
    y = []
    for j in range(9):
        y.append(grid[j][i])
    y = sorted(y)
    if y != one_to_nine:
        print("No")
        exit()

for i in range(9):
    z = []
    if i == 0:
        a = range(0, 3)
        b = range(0, 3)
    elif i == 1:
        a = range(3, 6)
        b = range(0, 3)
    elif i == 2:
        a = range(6, 9)
        b = range(0, 3)
    elif i == 3:
        a = range(0, 3)
        b = range(3, 6)
    elif i == 4:
        a = range(3, 6)
        b = range(3, 6)
    elif i == 5:
        a = range(6, 9)
        b = range(3, 6)
    elif i == 6:
        a = range(0, 3)
        b = range(6, 9)
    elif i == 7:
        a = range(3, 6)
        b = range(6, 9)
    elif i == 8:
        a = range(6, 9)
        b = range(6, 9)

    for j in a:
        for k in b:
            z.append(grid[j][k])
    z = sorted(z)
    if z != one_to_nine:
        print("No")
        exit()

print("Yes")

