n = int(input())
s = [0] + [*map(int, input().split())]
ansl = []
for i in range(1, n + 1):
    ansl.append(s[i] - s[i - 1])

print(*ansl)
