import sys
input = sys.stdin.readline
import math
import numpy

L = int(input())
x = L / 3
z = L - 2 * x
ans = x ** 2 * z
print(ans)

