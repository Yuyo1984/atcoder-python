N = int(input())
c1 = []
c2 = []
for i in range(N):
    c, p = map(int, input().split())
    if c == 1:
        c1.append((i, p))
    elif c == 2:
        c2.append((i, p))
