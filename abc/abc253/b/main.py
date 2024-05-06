h, w = map(int, input().split())
g = []
for i in range(h):
    g.append(list(input()))

o_p = []
for i in range(h):
    for j in range(w):
        if g[i][j] == 'o':
            o_p.append([i, j])

ans = abs(o_p[1][1] - o_p[0][1]) + abs(o_p[1][0] - o_p[0][0])
print(ans)
