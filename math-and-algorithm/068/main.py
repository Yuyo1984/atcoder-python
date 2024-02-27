import math
N, K = map(int, input().split())
V = [*map(int, input().split())]
ans = 0
for i in range(1, 1<<K):
    cnt = 0
    lcm = 1
    for j in range(K):
        if (i & (1 << j)) != 0:
            cnt += 1
            lcm = math.lcm(lcm, V[j])
    num = N // lcm
    if cnt % 2 == 1:
        ans += num
    else:
        ans -= num

print(ans)
