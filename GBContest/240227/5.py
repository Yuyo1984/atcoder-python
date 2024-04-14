import sys
input = sys.stdin.readline
import math
import numpy
from collections import Counter
N = int(input())
A = [*map(int, input().split())]

c = Counter(A)
print(c)
v_l = [kv[0] for kv in c.items() if kv[1] == max(c.values())]
print(v_l)
ansl = []
for i in range(len(v_l)):
    ansl.append([x for x in A if x != v_l[i]])
    print(ansl)

ansl.sort()
print(*ansl[0])
