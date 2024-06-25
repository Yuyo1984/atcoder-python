# input
N, M = map(int, input().split())
graph = {[] for i in range(N)}
for i in range(M):
    a, b, m = map(int, input().split())
    graph[a].append([b, i])
    graph[b].append([a, i])
# solve

# output
