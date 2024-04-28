N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())
P = [*map(int, input().split())]

ans = 0
for i in range(len(C)):
    if C[i] in D:
        n = D.index(C[i]) + 1
        ans += P[n]
    else:
        ans += P[0]

print(ans)

