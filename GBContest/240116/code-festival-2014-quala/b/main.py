import sys
input = sys.stdin.readline
import numpy as np

def count(x):
    y = len(a)
    x = x % y
    if x == 0:
        x = len(a)
    return x

a = list(input().rstrip())
b = int(input())
print(a[count(b) - 1])

