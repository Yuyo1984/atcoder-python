def make_word(start_points):
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    target_word = "snuke"
    for x in start_points:
        i = x[0]
        j = x[1]
        for d in range(8):
            move_x = dx[d]
            move_y = dy[d]
            Y = i
            X = j
            ansl = [[Y, X]]
            flag = True
            for k in range(1, 5):
                Y += move_x
                X += move_y
                if not (0 <= Y < h and 0 <= X < w):
                    flag = False
                    break
                s = grid[Y][X]
                if s != target_word[k]:
                    flag = False
                    break
                ansl.append([Y, X])

            if flag and len(ansl) == len(target_word):
                return ansl
    return []


h, w = map(int, input().split())
grid = []
for i in range(h):
    grid.append(list(input()))

start_points = []
for i in range(h):
    for j in range(w):
        if grid[i][j] == "s":
            start_points.append([i, j])

ansl = make_word(start_points)

for item in ansl:
    print(item[0] + 1, item[1] + 1)
