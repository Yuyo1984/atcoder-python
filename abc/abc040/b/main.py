import math

n = int(input())
x = int(math.sqrt(n))
ansl = []
for i in range(1, x + 1):
    j = n // i
    ans = n - (i * j) + abs(i - j)
    ansl.append(ans)

ansl.sort(reverse=True)
print(ansl[-1])
