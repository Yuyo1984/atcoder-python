from collections import deque

T = deque()
Q = int(input())
for i in range(Q):
    query = list(input().split())
    q_t = query[0]
    if q_t == "1":
        T.append(query[1])
    elif q_t == "2":
        print(T[0])
    elif q_t == "3":
        T.popleft()
