from itertools import count

n = int(input())
ansl = []

for i in count(1):
    if i * i > n:
        break
    if n % i != 0:
        continue
    ansl.append(i)
    if i != n // i:
        ansl.append(n // i)

ansl.sort()
print(ansl)
