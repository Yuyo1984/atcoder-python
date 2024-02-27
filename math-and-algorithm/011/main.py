n = int(input())

p_n = []

for i in range(2, n+1):
    flag = True
    for j in range(2, i):
        if j != i and i % j == 0:
            flag = False
    if flag:
        p_n.append(i)

print(*p_n)

