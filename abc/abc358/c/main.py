# input
n, m = map(int, input().split())
S = [list(input()) for i in range(n)]
ans = n

# solve
for i in range(1 << n):
    cnt = 0
    flag = [False] * m
    for j in range(n):
        if i & (1 << j):
            cnt += 1
            for k in range(m):
                if S[j][k] == "o":
                    flag[k] = True
    if all(flag):
        ans = min(cnt, ans)

# output
print(ans)
