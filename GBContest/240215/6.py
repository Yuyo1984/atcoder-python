import sys
input = sys.stdin.readline
import math
import numpy

S = input().rstrip()

print((min(S.count('1'), S.count('0')) * 2))
