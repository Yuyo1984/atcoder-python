n = int(input())
w = [*map(int, input().split())]

ansl = []


for i in range(n):
    a1 = 0
    a2 = 0
    for j in range(n):
        if j <= i:
            a1 += w[j]
        else:
            a2 += w[j]

    ansl.append(abs(a2 - a1))

print(min(ansl))
