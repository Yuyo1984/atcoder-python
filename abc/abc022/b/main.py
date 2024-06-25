import collections

N = int(input())
flag = [False] * (10**5 + 9)

ans = 0
for i in range(N):
    x = int(input())
    if flag[x]:
        ans += 1
    else:
        flag[x] = True
print(ans)
