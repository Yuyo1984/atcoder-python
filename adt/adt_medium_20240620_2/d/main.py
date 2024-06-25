# 解説AC
# input
N, M = map(int, input().split())
# 自分より強い人の人数を管理する配列
S = [0] * N
# solve
for i in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    S[b] += 1

# output
ans = -1
for i in range(N):
    if S[i] == 0:
        if ans != -1:
            print(-1)
            exit()
        else:
            ans = i + 1

print(ans)
