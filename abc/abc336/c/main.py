from sys import stdin
input = stdin.readline
import numpy as np

n = int(input()) - 1
print(2*int(np.base_repr(n, 5)))
