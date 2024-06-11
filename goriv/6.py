import sys

sys.setrecursionlimit(10**6)


def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def search_connected(graph, n):
    start_node = n
    visited = set()
    dfs(graph, start_node, visited)

    return visited


n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


ans = 0
visited = set()
for i in range(1, n + 1):
    if i not in visited:
        visited = visited | search_connected(graph, i)
        ans += 1

print(ans)
