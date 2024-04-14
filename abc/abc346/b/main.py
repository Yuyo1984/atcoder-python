import sys
input = sys.stdin.readline
import numpy as np
import math

w, b = map(int, input().split())
S = 'wbwbwwbwbwbw' * 20

x = len(S) - w - b - 1
for i in range(x):
    T = S[i:i+w+b]
    if T.count('w') == w and T.count('b') == b:
        print("Yes")
        exit()

print("No")


