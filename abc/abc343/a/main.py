import sys
input = sys.stdin.readline
import numpy as np
import math

A, B = map(int, input().split())
x = A + B
for i in range(0, 10):
    if i != x:
        print(i)
        exit()
