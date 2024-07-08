# input
N, M = map(int, input().split())
P = []
C = []
F = []
for i in range(N):
    p, c, *f = map(int, input().split())
    P.append(p)
    C.append(c)
    F.append(set(list(f)))
# solve
flag = False
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if P[i] >= P[j]:
            if F[i] <= F[j]:
                if P[i] > P[j] or F[j] > F[i]:
                    flag = True
    if flag:
        print("Yes")
        exit()
# output
print("No")
