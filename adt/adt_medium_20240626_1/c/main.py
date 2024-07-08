# input
N = int(input())
sheet = [[False for i in range(101)] for j in range(101)]
# solve
for i in range(N):
    a, b, c, d = map(int, input().split())
    for j in range(a, b):
        for k in range(c, d):
            sheet[j][k] = True
# output
ans = 0
for i in range(101):
    for j in range(101):
        if sheet[i][j]:
            ans += 1

print(ans)
