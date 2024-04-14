from sys import stdin
input = stdin.readline
import numpy as np

N, K = map(int, input().split())

print(len(np.base_repr(N, K)))
