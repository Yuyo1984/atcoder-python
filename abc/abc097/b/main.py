X = int(input())

ansl = []
for p in range(2, 11):
    for b in range(1, 33):
        x = b**p
        if x not in ansl and x:
            ansl.append(x)

ansl.sort(reverse=True)

for a in ansl:
    if a <= X:
        print(a)
        exit()
