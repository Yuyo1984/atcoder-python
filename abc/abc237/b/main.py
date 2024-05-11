h, w = map(int, input().split())

m = []
for i in range(h):
    m.append(list(map(int, input().split())))


m = [list(x) for x in zip(*m)]

for i in range(w):
    print(*m[i])
