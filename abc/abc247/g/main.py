from collections import defaultdict

N = int(input())
F_N = defaultdict(list)
L_N = defaultdict(list)
for i in range(N):
    s, t = input().split()
    F_N[s].append(t)
    L_N[t].append(s)

flag = True
for x in F_N:
    if len(x.values) >= 2:
        for y in L_N:
            if len(y.values) >= 2:
                flag = False

if flag:
    print("Yes")
else:
    print("No")
