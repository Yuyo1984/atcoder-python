# input
N, M, K = map(int, input().split())

key = [[0 for i in range(N)] for i in range(M)]
r = []

for i in range(M):
    query = list(input().split())
    c = int(query[0])
    A = [int(i) for i in query[1:-1]]
    for a in A:
        key[i][a - 1] = 1
    r.append(query[-1])

res = 0
for i in range(1 << N):
    tf = [0] * N
    for j in range(N):
        if i & (1 << j):
            tf[j] = 1
        else:
            tf[j] = 0
    jud = True
    for j in range(M):
        ck = 0
        for p in range(N):
            if key[j][p] == 1 and tf[p] == 1:
                ck += 1
        if ck >= K and r[j] == "x":
            jud = False
        if ck < K and r[j] == "o":
            jud = False
    if jud:
        res += 1

print(res)
