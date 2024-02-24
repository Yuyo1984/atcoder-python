import sys
input = sys.stdin.readline
import numpy as np

N = int(input())
A = [*map(int, input().split())]
square = []
i = 0
x = 2 * 10 ** 5
while i * i <= x:
    square.append(i * i)
    i += 1


