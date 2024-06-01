from collections import defaultdict


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited


def is_connected(graph):
    start_node = next(iter(graph))
    visited = dfs_iterative(graph, start_node)

    return len(visited) == len(graph)


graph = defaultdict(list)
n, m = map(int, input().split())
for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

if is_connected(graph):
    print("The graph is connected.")
else:
    print("The graph is not connected.")
