n = int(input())
c1 = {"H", "D", "C", "S"}
c2 = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"}
t_l = []

for i in range(n):
    x = input()
    if x not in t_l:
        t_l.append(x)
    else:
        print("No")
        exit()

for i in range(n):
    if t_l[i][0] not in c1:
        print("No")
        exit()
    if t_l[i][1] not in c2:
        print("No")
        exit()

print("Yes")
