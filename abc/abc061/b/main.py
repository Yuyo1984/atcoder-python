n, m = map(int, input().split())

graph = {i + 1: [] for i in range(n)}

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for x in range(n):
    print(len(graph[x + 1]))
