# input
N, Q = map(int, input().split())
S = input()
mod = N
cnt = 0
# solve
for i in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        x %= mod
        cnt -= x
        cnt %= mod
    elif t == 2:
        print(S[(x + cnt - 1) % mod])
# output
