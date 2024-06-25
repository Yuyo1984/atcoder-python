s = int(input())
l = [s]
i = 0
while True:
    if l[i] % 2 == 0:
        l.append(l[i] // 2)
    else:
        l.append(l[i] * 3 + 1)
    i += 1
    if l.count(l[i]) == 2:
        print(i + 1)
        exit()
