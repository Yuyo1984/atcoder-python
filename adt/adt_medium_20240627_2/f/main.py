from collections import defaultdict

# input
N = int(input())
beans = defaultdict(list)
# solve
for i in range(N):
    a, c = map(int, input().split())
    beans[c].append(a)

L = [min(x) for x in beans.values()]
# output
print(max(L))
