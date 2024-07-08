import collections
import math

# input
N = int(input())
rate_d = collections.defaultdict(list)
p = collections.defaultdict(int)
s = []
# solve
for i in range(N):
    a, b = map(int, input().split())
    x = a + b
    s.append(x)
    rate_d[i + 1].append(a)
    rate_d[i + 1].append(b)

g = math.lcm(*s)
# output
for i in range(1, N + 1):
    x = rate_d[i][0]
    y = rate_d[i][1]
    p[i] = x * (g // y)

p = sorted(p.items(), key=lambda x: x[1], reverse=True)
ansl = []
for x in p:
    ansl.append(x[0])
print(*ansl)
