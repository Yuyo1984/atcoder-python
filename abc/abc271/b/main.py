n, q = map(int, input().split())
seq = []
for i in range(n):
    l, *a = map(int, input().split())
    seq.append([*a])

for i in range(q):
    s, t = map(int, input().split())
    print(seq[s-1][t-1])
