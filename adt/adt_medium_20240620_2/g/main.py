# input
N, K = map(int, input().split())
A = [*map(int, input().split())]
# solve
ok = 0
ng = (10**18) // K
while (ng - ok) > 1:
    md = (ok + ng) // 2
    sum = 0
    for x in A:
        sum += min(x, md)
    if sum >= K * md:
        ok = md
    else:
        ng = md

# output
print(ok)
