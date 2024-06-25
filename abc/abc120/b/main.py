a, b, k = map(int, input().split())
ansl = []
for i in range(min(a, b) + 1, 0, -1):
    if a % i == 0 and b % i == 0:
        ansl.append(i)

print(ansl[k - 1])
