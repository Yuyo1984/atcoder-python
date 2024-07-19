import sys

sys.setrecursionlimit(10**6)


# Depth First Search
#
def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# n, m = map(int, input().split())
# graph = {i: [] for i in range(1, n + 1)}
# for i in range(m):
# a, b = map(int, input().split())
# graph[a].append(b)
# graph[b].append(a)
