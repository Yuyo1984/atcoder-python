N, K = map(int, input().split())

A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)


l = 1 << 30
r = 0
ans = 0
while abs(l - r) > 1:
    m = (l + r) // 2
    s = 0
    for i in range(N):
        if m <= A[i]:
            s += B[i]
    if s <= K:
        l = m
    elif s > K:
        r = m
print(l)
