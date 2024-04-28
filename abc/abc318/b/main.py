N = int(input())
points = []
for i in range(N):
    a, b, c, d = map(int, input().split())
    points.append([a, b, c, d])

A = [[0 for i in range(101)] for j in range(101)]

for i in range(N):
    for j in range(points[i][2], points[i][3]):
        for k in range(points[i][0], points[i][1]):
            A[j][k] += 1

ans = 0
for i in range(101):
    for j in range(101):
        if A[i][j] > 0:
            ans += 1

print(ans)

