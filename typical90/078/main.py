N, M = map(int, input().split())
graph = {i + 1: [] for i in range(N)}

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0

for i in range(N):
    g = graph[i + 1]
    cnt = 0
    for x in g:
        if x < i + 1:
            cnt += 1
    if cnt == 1:
        ans += 1

print(ans)
