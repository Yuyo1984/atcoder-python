N = list(map(int, input()))

for i in range(1 << 3):
    res = N[0]
    ansl = [str(N[0])]
    for j in range(1, 4):
        if i & (1 << j):
            ansl.append("+")
            res += N[j]
        else:
            ansl.append("-")
            res -= N[j]
        ansl.append(str(N[j]))
    if res == 7:
        ansl.append("=")
        ansl.append("7")
        print("".join(ansl))
        exit()
