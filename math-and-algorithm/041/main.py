from itertools import accumulate

T = int(input())
N = int(input())
imos = [0] * (T + 1)

for i in range(N):
    l, r = map(int, input().split())
    imos[l] += 1
    imos[r] -= 1

ansl = list(accumulate(imos))
for x in range(len(ansl) - 1):
    print(ansl[x])
