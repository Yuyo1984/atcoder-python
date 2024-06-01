N, M = map(int, input().split())
graph = [[] for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    d = len(graph[i])
    graph[i].sort()
    print(d, *graph[i])
