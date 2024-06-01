# import sys

# sys.setrecursionlimit(10**6)


def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def is_connected(graph, n):
    start_node = 1
    visited = set()
    dfs(graph, start_node, visited)

    return len(visited) == n


n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

if is_connected(graph, n):
    print("The graph is connected.")
else:
    print("The graph is not connected.")
