n, a, b = map(int, input().split())
ans = []
y_ch = 0
x_ch = 0
for i in range(a * n):
    if i == 0:
        pass
    else:
        if (i + 1) % a == 0:
            y_ch ^= 1
    ans_line = []

    for j in range(b * n):
        if j == 0:
            pass
        else:
            if (j + 1) % b == 0:
                x_ch ^= 1
        if y_ch ^ x_ch:
            ans_line.append("#")
        else:
            ans_line.append(".")
    ans.append(ans_line)

for i in range(a * n):
    print("".join(ans[i]))
