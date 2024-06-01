from sortedcontainers import SortedSet


def binary_search(sorted_set, x):
    idx = sorted_set.bisect_left(x)
    if idx < len(sorted_set):
        return sorted_set[idx]
    else:
        return -1


sorted_set = SortedSet()
Q = int(input())
queries = [map(int, input().split()) for i in range(Q)]

for q_t, x in queries:
    if q_t == 1:
        sorted_set.add(x)
    elif q_t == 2:
        sorted_set.discard(x)
    elif q_t == 3:
        print(binary_search(sorted_set, x))
