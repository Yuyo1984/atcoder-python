N, M = map(int, input().split())
S = []
for i in range(N):
    S.append(list(input()))


ans = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(M):
            flag = True
            if S[i][k] == 'x' and S[j][k] == 'x':
                flag = False
                break
        if flag:
            ans += 1

print(ans)
