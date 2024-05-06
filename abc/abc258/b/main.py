n = int(input())
box = []
for i in range(n):
    box.append(list(map(int, input())))
move_x = [-1, 0, 1, -1, 1, -1, 0, 1]
move_y = [-1, -1, -1, 0, 0, 1, 1, 1]
x = 0
start = []
for i in range(n):
    for j in range(n):
        if box[i][j] > x:
            x = box[i][j]
            start.clear()
        if x == box[i][j]:
            start.append([i, j])
        if x == 9:
            break

checker = 0
next = []
direction = []
for s in start:
    n_s = []
    d_s = []
    for i in range(8):
        Y = s[0]+move_y[i]
        X = s[1]+move_x[i]
        if Y < 0:
            Y = n-1
        if Y >= n:
            Y = 0
        if X < 0:
            X = n-1
        if X >= n:
            X = 0
        if box[Y][X] > checker:
            checker = box[Y][X]
            n_s.clear()
            d_s.clear()
        if checker == box[Y][X]:
            n_s.append([Y, X])
            d_s.append(i)
        print(n_s)
    next.append(n_s)
    direction.append(d_s)

print(next[0][0][0])
print(next[0][0][1])
print(direction[0][0])







    

