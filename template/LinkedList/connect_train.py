n, q = map(int, input().split())

nex = [-1 for _ in range(N)]
bak = [-1 for _ in range(N)]

for i in range(q):
    query = [*map(int, input().split())]
    q_t = query[0]

    if q_t == 0:
        p, q = query[1], query[2]
        nex[p] = q
        bak[q] = p

    elif q_t == 1:
        r = query[1]

        if nex[r] != -1:
            bak[nex[r]] = bak[r]
        if bak[r] != -1:
            nex[bak[r]] = nex[r]

        nex[r] = bak[r] = -1

ans, now = 0, 0

while now != -1:
    ans += 1
    now = nex[now]

now = 0
while now != -1:
    ans += 1
    now = bak[now]

ans -= 1
print(ans)
