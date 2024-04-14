K, X = map(int, input().split())
a = X - K + 1
b = X + K
ansl = []
for i in range(a, b):
    ansl.append(i)

print(*ansl)
