import sys
input = sys.stdin.readline
import numpy as np

from collections import Counter
S = input().rstrip()
c = Counter(S)
x = [k for k,v in c.items() if v == 1]
print(S.index(x[0])+1)
