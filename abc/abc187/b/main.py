N = int(input())
ans = 0
points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append([x, y])

for i in range(N):
    for j in range(i, N):
        b = points[j][1] - points[i][1]
        a = points[j][0] - points[i][0]
        if a == 0:
            continue
        r = b / a
        if -1 <= r <= 1:
            ans += 1

print(ans)

