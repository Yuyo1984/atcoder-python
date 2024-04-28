N, M = map(int, input().split())

a = []
for i in range(M):
    a.append([*map(int, input().split())])

ans = 0

for i in range(1, N+1):
    for j in range(i+1, N+1):
        flag = False
        for k in range(M):
            for l in range(N-1):
                if a[k][l] == i and a[k][l+1] == j:
                    flag = True

                if a[k][l] == j and a[k][l+1] == i:
                    flag = True

        if not(flag):
            ans += 1

print(ans)
