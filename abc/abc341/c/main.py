def move(q):
    m_w = [-1, 0, 1, 0]
    m_h = [0, -1, 0, 1]
    if q == 'L':
        return [m_h[0], m_w[0]]
    elif q == 'U':
        return [m_h[1], m_w[1]]
    elif q == 'R':
        return [m_h[2], m_w[2]]
    else:
        return [m_h[3], m_w[3]]

H, W, N = map(int, input().split())
T = input()
grid = [[] for i in range(H)]
s_p = []
for i in range(H):
    line = list(input().rstrip())
    for j in range(len(line)):
        if line[j] == '#':
            grid[i].append(False)
        else:
            grid[i].append(True)
            s_p.append([i, j])

ans = 0
for i in s_p:
    now_p = i
    x = now_p[1]
    y = now_p[0]
    for j in range(N):
        m = move(T[j])
        x += m[1]
        y += m[0]
        if not(grid[y][x]):
            break
        if j == N-1:
            ans += 1
            break

print(ans)

