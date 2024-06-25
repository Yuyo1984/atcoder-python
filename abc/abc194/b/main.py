N = int(input())
la = []
lb = []
lc = []
for i in range(N):
    a, b = map(int, input().split())
    c = a + b
    la.append(a)
    lb.append(b)
    lc.append(c)
m_c = min(lc)
m_ab = 10**6
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        x = max(la[i], lb[j])
        if x <= m_ab:
            m_ab = x

ans = min(m_ab, m_c)
print(ans)
