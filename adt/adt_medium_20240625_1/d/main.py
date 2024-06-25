from collections import defaultdict

# input
N = int(input())
d = defaultdict(list)
cnt = [0 for i in range(N + 1)]

for i in range(N):
    c = int(input())
    cnt[i + 1] += c
    A = [*map(int, input().split())]
    for j in range(c):
        d[A[j]].append(i + 1)

x = int(input())
ansl = []
min = 100
for i in range(len(d[x])):
    if min >= cnt[d[x][i]]:
        min = cnt[d[x][i]]

for a in d[x]:
    if cnt[a] == min:
        ansl.append(a)

print(len(ansl))
print(*ansl)
