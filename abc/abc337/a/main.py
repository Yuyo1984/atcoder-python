import sys
input = sys.stdin.readline
import numpy as np

n = int(input())
xy = []
for i in range(n):
    xy.append([*map(int, input().split())])
x_p, y_p = 0, 0
for i in range(n):
    x_p += xy[i][0]
    y_p += xy[i][1]

if x_p > y_p:
    print("Takahashi")
elif x_p < y_p:
    print("Aoki")
else:
    print("Draw")

