# input
n, m = map(int, input().split())
c = list(input().split())
d = list(input().split())
p = [*map(int, input().split())]
pz = p.pop(0)
# solve
ans = 0
for i in range(n):
    if c[i] not in d:
        ans += pz
    else:
        ans += p[d.index(c[i])]
# output
print(ans)
