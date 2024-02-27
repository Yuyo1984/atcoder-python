H, W = map(int, input().split())
cross = []
ans = [[0 for i in range(W)] for j in range(H)]
for i in range(H):
    cross.append([*map(int, input().split())])
sum_H = [0] * H
sum_W = [0] * W
for i in range(H):
    sum_H[i] = sum(cross[i])

for i in range(W):
    for j in range(H):
        sum_W[i] += cross[j][i]

for i in range(H):
    for j in range(W):
        ans[i][j] = sum_H[i] + sum_W[j] - cross[i][j]

for i in range(H):
    print(*ans[i])
