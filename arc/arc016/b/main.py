# func

# input
n = int(input())
g = []
for i in range(n):
    g.append(list(input()))
# solve
ans = 0
for j in range(9):
    Flag = False
    for i in range(n):
        if g[i-1][j] == 'x':
            ans += 1
        if g[i][j] == 'o':
            Flag = True
        if (g[i][j] != 'o' or i == n-1) and Flag:
            ans += 1
            Flag = False
# answer
print(ans)
