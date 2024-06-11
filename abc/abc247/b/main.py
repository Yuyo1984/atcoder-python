from collections import defaultdict

N = int(input())
F_N = defaultdict(list)
L_N = defaultdict(list)
for i in range(N):
    s, t = input().split()
    F_N[s].append(t)
    L_N[t].append(s)

flag = True
print(*F_N.items)
print(*L_N.items)

if flag:
    print("Yes")
else:
    print("No")
