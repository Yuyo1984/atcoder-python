h, w = map(int, input().split())
l_a = []
l_b = []
for i in range(h):
    line = list(input())
    for j in range(w):
        if line[j] == "#":
            l_a.append([i, j])

for i in range(h):
    line = list(input())
    for j in range(w):
        if line[j] == "#":
            l_b.append([i, j])

if len(l_a) != len(l_b):
    print("No")
    exit()

s = (abs(l_a[0][0] - l_b[0][0])) % h
t = (abs(l_a[0][1] - l_b[0][1])) % w
print(s, t)
for i in range(1, len(l_a) + 1):
    m_h = (abs(l_a[i][0] - l_b[i][0])) % h
    m_w = (abs(l_a[i][1] - l_b[i][1])) % w
    print(m_h, m_w)
    if s != m_h or t != m_w:
        print("No")
        exit()

print("Yes")
