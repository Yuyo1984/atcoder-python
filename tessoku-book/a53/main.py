import heapq

heap = []
Q = int(input())

for i in range(Q):
    query = list(map(int, input().split()))
    q_t = query[0]
    if q_t == 1:
        heapq.heappush(heap, query[1])
    elif q_t == 2:
        print(heap[0])
    elif q_t == 3:
        heapq.heappop(heap)
