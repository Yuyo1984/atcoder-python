# input
N, M = map(int, input().split())
s_l = []
for i in range(M):
    c = int(input())
    s_l.append(set(map(int, input().split())))

ans = 0
sample = set([i for i in range(1, N + 1)])
# solve
for i in range(1 << M):
    s = set()
    for j in range(M):
        if i & (1 << j):
            s |= s_l[j]
    if s == sample:
        ans += 1

# output
print(ans)
