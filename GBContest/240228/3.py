import sys
input = sys.stdin.readline
import math
import numpy as np

N = int(input())
A = [*map(int, input().split())]

if A.count() > N // 2:
    print("No")
else:
    print("Yes")

