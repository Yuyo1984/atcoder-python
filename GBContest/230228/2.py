import sys
input = sys.stdin.readline
import math
import numpy

S, T, X = map(int, input().split())

if S > T:
    T += 24
if S > X:
    X += 24

if S <= X < T:
    print("Yes")
else:
    print("No")
