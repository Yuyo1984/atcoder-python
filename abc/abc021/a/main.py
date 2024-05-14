n = int(input())

ansl = []

while n > 2:
    n -= 2
    ansl.append(2)

ansl.append(n)

print(len(ansl))
for x in ansl:
    print(x)
