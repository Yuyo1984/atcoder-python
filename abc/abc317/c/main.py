import heapq


def dijkstra(graph, start):
    distances = {node: float("-inf") for node in graph}


N, M = map(int, input().split())
