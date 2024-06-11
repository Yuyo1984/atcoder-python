import collections

n, t = map(int, input().split())
C = [*map(int, input().split())]
R = [*map(int, input().split())]
cr_dict = collections.defaultdict(list)
for i in range(n):
    cr_dict[C[i]].append(R[i])

if C.count(t) >= 1:
    x = max(cr_dict[t])
    print(R.index(x) + 1)
else:
    x = max(cr_dict[C[0]])
    print(R.index(x) + 1)
