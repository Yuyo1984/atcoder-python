from sys import stdin
input = stdin.readline
from collections import deque

INF = -2**30
R, C = map(int, input().split())
sy, sx = map(int, input().split())
sy -= 1
sx -= 1
gy, gx = map(int, input().split())
gy -= 1
gx -= 1

maze = []
for i in range(R):
    maze.append(list(input().rstrip()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():
    d = list()
    for i in range(R):
        l = list()
        for j in range(C):
            l.append(INF)
        d.append(l)

    q = deque()
    q.append([sy, sx])
    d[sy][sx] = 0
    while len(q) != 0:
        p = q.popleft()
        if p[0] == gy and p[1] == gx:
            break
        for i in range(4):
            nx = p[1] + dx[i]
            ny = p[0] + dy[i]

            if 0 <= nx < C and 0 <= ny < R and maze[ny][nx] != '#' and d[ny][nx] == INF:
                q.append([ny, nx])
                d[ny][nx] = d[p[0]][p[1]] + 1

    return d[gy][gx]

ans = bfs()
print(ans)

