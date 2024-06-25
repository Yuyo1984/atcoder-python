# input
h, w = map(int, input().split())
C = []
for i in range(h):
    C.append(list(input()))
ansl = []
# solve
for j in range(w):
    cnt = 0
    for i in range(h):
        if C[i][j] == "#":
            cnt += 1
    ansl.append(cnt)
# output
print(*ansl)
