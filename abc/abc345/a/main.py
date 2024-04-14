import sys
input = sys.stdin.readline
import numpy as np
import math
import itertools

S = input().rstrip()
x = len(S)-1

if S[1:x] == '=' * (x-1) and S[0] == '<' and S[x] == '>':
    print("Yes")
else:
    print("No")

