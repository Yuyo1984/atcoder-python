def rotate_v_l(x, y):
    return (-y, x)


x1, y1, x2, y2 = map(int, input().split())

dx = x2 - x1
dy = y2 - y1

dx, dy = rotate_v_l(dx, dy)
x3 = x2 + dx
y3 = y2 + dy
dx, dy = rotate_v_l(dx, dy)
x4 = x3 + dx
y4 = y3 + dy
print(x3, y3, x4, y4)
