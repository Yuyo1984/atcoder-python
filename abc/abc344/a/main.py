import sys
input = sys.stdin.readline
import numpy as np
import math

S = input().rstrip()

x = S.index("|")
y = S.rindex("|")
print(S[0:x]+S[y+1:])

