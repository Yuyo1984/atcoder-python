#input
n = int(input())
cards_spec = []
ansl = []
for i in range(n):
    a, c = map(int, input().split())
    cards_spec.append([a, c, i+1])
#solve
cards_spec = sorted(cards_spec, key=lambda x:x[1])
v = 0
for i in range(n):
    if cards_spec[i][0] > v:
        ansl.append(cards_spec[i][2])
        v = cards_spec[i][0]
#output
print(len(ansl))
ansl.sort()
print(*ansl)
