h, w = map(int, input().split())
g = []
for i in range(h):
    g.append(list(input()))

ansl = []
for i in range(w):
    ans = 0
    for j in range(h):
        if g[j][i] == '#':
            ans += 1
    ansl.append(ans)

print(*ansl)

