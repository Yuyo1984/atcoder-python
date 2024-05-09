h, w = map(int, input().split())
p = []
for i in range(h):
    p.append(list(input()))

for i in range(h):
    for j in range(2):
        print(''.join(p[i]))

