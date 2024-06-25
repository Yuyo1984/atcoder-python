n, m = map(int, input().split())
ab = []
cd = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append([a, b])
for j in range(m):
    c, d = map(int, input().split())
    cd.append([c, d])

for i in range(n):
    x = ab[i]
    d = float("inf")
    ans = m + 1
    for j in range(m):
        y = cd[j]
        m_d = abs(x[0] - y[0]) + abs(x[1] - y[1])
        if m_d < d:
            ans = j + 1
            d = m_d
    print(ans)
