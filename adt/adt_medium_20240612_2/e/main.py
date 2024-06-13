# input
h, w = map(int, input().split())
A = [[*map(int, input().split())] for i in range(h)]
# solve
ans = 0
l = h + w - 2
for i in range(2**l):
    x, y = 0, 0
    s = set()
    s.add(A[0][0])

    for j in range(h + w - 2):
        if i >> j & 1:
            x += 1
            if x == h:
                break
            if A[x][y] in s:
                break
        else:
            y += 1
            if y == w:
                break
            if A[x][y] in s:
                break
        s.add(A[x][y])
    if len(s) == l + 1:
        ans += 1
# output
print(ans)
