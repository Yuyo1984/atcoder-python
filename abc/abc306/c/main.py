from collections import defaultdict

n = int(input())
a = [*map(int, input().split())]

d = defaultdict(list)

for i in range(len(a)):
    d[a[i]].append(i+1)

ranking = defaultdict(int)

for i in range(1, n+1):
    ranking[i] = d[i][1]

ranking = sorted(ranking.items(), key=lambda x:x[1])

ansl = []
for i in range(n):
    ansl.append(ranking[i][0])

print(*ansl)
