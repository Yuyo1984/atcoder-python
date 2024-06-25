# input
N, D = map(int, input().split())
S = [list(input()) for i in range(N)]

# solve
ans = 0
cnt = 0
for i in range(D):
    flag = True
    for j in range(N):
        if S[j][i] == "x":
            flag = False
    if flag:
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0

# output
print(ans)
