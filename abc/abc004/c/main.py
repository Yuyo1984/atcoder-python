import sys
input = sys.stdin.readline
import numpy as np
import math

N = int(input())
seq = [str(i) for i in range(1, 7)]

cnt = (N // 5) % 6
rem = N % 5

seq = seq[cnt:] + seq[0:cnt]
for i in range(0, rem):
    seq[i],seq[i+1] = seq[i+1],seq[i]
print(''.join(seq))


