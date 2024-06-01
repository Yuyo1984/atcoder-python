from collections import deque


def bfs(graph, start):
    distances = {node: -1 for node in graph}
    distances[start] = 0
    queue = deque([start])

    while queue:
        current = queue.popleft()
        current_distance = distances[current]

        for neighbor in graph[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = current_distance + 1
                queue.append(neighbor)

    return distances


n, m = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

start_node = 1
distances = bfs(graph, start_node)

for node in range(1, n + 1):
    print(distances[node])
