import sys
input = sys.stdin.readline
import math
import numpy

T = int(input())
for i in range(T):
    N = int(input())
    flag = False
    for a in range(1, N//2):
        for b in range(a+1, N//2):
            c = N - a - b
            if math.lcm(a, b, c) == N:
                flag = True
                break
        if flag:
            break
    if flag:
        print("Yes")
    else:
        print("No")

