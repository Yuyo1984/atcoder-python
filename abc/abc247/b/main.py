N = int(input())
n_l = []
for i in range(N):
    s, t = input().split()
    n_l.append([s, t])


flag1 = False
flag2 = False
for i in range(N):
    f1 = n_l[i][0]
    l1 = n_l[i][1]
    for j in range(N):
        if i == j:
            continue
        f_n = n_l[j][0]
        l_n = n_l[j][1]
        if l_n == l1 or l_n == f1:
            flag1 = True
        if f_n == f1 or f_n == l1:
            flag2 = True
        if flag1 and flag2:
            print("No")
            exit()

print("Yes")
