N, M = map(int, input().split())
S = []
T = []

for i in range(N):
    S.append(input())

for i in range(M):
    T.append(input())

ans = 0

for i in range(N):
    if S[i][3:6] in T:
        ans += 1

print(ans)

