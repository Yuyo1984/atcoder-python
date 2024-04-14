import sys

input = sys.stdin.readline
import math

import numpy as np

N = int(input())
A = [*map(int, input().split())]

print(-sum(A))
