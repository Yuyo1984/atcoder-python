import math

N, D = map(int, input().split())
points = []

for i in range(N):
    points.append([*map(int, input().split())])

ans = 0
for i in range(N):
    for j in range(i+1, N):
        x = 0
        for k in range(D):
            x += (points[i][k] - points[j][k])**2
        x = math.sqrt(x)
        if x.is_integer():
            ans += 1

print(ans)

