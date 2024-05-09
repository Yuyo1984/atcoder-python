n, m = map(int, input().split())
p_l = []
c_l = []
f_l = []
for i in range(n):
    p, c, *f = map(int, input().split())
    p_l.append(p)
    c_l.append(c)
    f_l.append(list(f))

for i in range(n):
    for j in range(n):
        flag = True
        if i == j or p_l[i] < p_l[j]:
            continue
        for idx in range(len(f_l[i])):
            if f_l[i][idx] not in f_l[j]:
                flag = False
        if flag:
            if p_l[i] > p_l[j] or c_l[j] > c_l[i]:
                print("Yes")
                exit()

print("No")

