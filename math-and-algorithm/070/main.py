def cnt_points(lx, rx, ly, ry):
    cnt = 0
    for i in range(N):
        if lx <= x_l[i] and x_l[i] <= rx and ly <= y_l[i] and y_l[i] <= ry:
            cnt += 1
    return cnt

N, K = map(int, input().split())
x_l = []
y_l = []
ans = 1<<62

for i in range(N):
    x, y = map(int, input().split())
    x_l.append(x)
    y_l.append(y)

for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):
                cl = x_l[i]
                cr = x_l[j]
                dl = y_l[k]
                dr = y_l[l]
                if cl < cr and dl < dr:
                    if cnt_points(cl, cr, dl, dr) >= K:
                        area = (cr - cl) * (dr - dl)
                        ans = min(area, ans)

print(ans)

