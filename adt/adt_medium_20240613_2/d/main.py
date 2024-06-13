import math

# input
N = int(input())
p_l = []
ans = -1
# solve
for i in range(N):
    x, y = map(int, input().split())
    p_l.append([x, y])

for i in range(N):
    for j in range(N):
        d = math.sqrt((p_l[j][0] - p_l[i][0]) ** 2 + (p_l[j][1] - p_l[i][1]) ** 2)
        if d >= ans:
            ans = d
# output
print(ans)
