N, Q = map(int, input().split())

relation = [[0 for _ in range(N)] for _ in range(N)]
cnt_followers = [0] * N
for i in range(Q):
    query = [*map(int, input().split())]
    q_t = query[0]
    if q_t == 0:
        x, y = query[1], query[2]
        if relation[x][y] == 0:
            relation[x] += 1
            cnt_followers[x] += 1
    elif q_t == 1:
        x, y = query[1], query[2]
        if relation[x][y] == 1:
            relation[x][y] -= 1
            cnt_followers[x] -= 1
    elif q_t == 2:
        z = query[1]
        print(cnt_followers[z])

