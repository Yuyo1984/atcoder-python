def rotate(grid):
    grid = grid[::-1]
    grid = list(map(list, zip(*grid)))
    return grid


N = int(input())
s = [list(input()) for i in range(N)]
s = rotate(s)
for i in range(N):
    print("".join(s[i]))
