# input
N, T = map(int, input().split())
card = [[False for _ in range(N)] for _ in range(N)]
A = [*map(int, input().split())]
r_cnt = [0] * N
c_cnt = [0] * N
cross1_cnt = 0
cross2_cnt = 0
turn_cnt = 0
# solve
for a in A:
    x = (a - 1) // N
    y = (a - 1) % N
    card[x][y] = True
    turn_cnt += 1

    r_cnt[x] += 1
    c_cnt[y] += 1
    if x == y:
        cross1_cnt += 1
    if x + y == N - 1:
        cross2_cnt += 1

    if r_cnt[x] == N or c_cnt[y] == N or cross1_cnt == N or cross2_cnt == N:
        print(turn_cnt)
        exit()
# output
print(-1)
