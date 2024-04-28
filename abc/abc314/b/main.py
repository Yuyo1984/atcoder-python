N = int(input())
A = []
B = {}
for i in range(N):
    C = int(input())
    B[i+1] = C
    A.append([*map(int, input().split())])

X = int(input())
targets = []
for i in range(N):
    if X in A[i]:
        targets.append(i+1)

ansl = []

c = 38
for a, b in B.items():
    if a in targets and b <= c:
        c = b

for i in range(len(targets)):
    x = B[targets[i]]
    if x == c:
        ansl.append(targets[i])

print(len(ansl))
print(*ansl)
