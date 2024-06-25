x = int(input())
x = 2025 - x
ansl = []
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == x:
            ansl.append([i, j])

for x in ansl:
    print(str(x[0]) + " x " + str(x[1]))
