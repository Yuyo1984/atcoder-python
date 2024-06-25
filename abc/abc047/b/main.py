w, h, n = map(int, input().split())
pic = [[1 for j in range(w)] for i in range(h)]
for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        for i in range(h):
            for j in range(x):
                pic[i][j] = 0
    elif a == 2:
        for i in range(h):
            for j in range(x, w):
                pic[i][j] = 0
    elif a == 3:
        for i in range(y):
            for j in range(w):
                pic[i][j] = 0
    else:
        for i in range(y, h):
            for j in range(w):
                pic[i][j] = 0

ans = 0
for i in range(h):
    for j in range(w):
        ans += pic[i][j]

print(ans)
