from sys import stdin
input = stdin.readline
import math

A, B = map(int, input().split())
x = 1
while x < 1010:
    if (math.floor(x*0.08) == A) and (math.floor(x*0.1) == B):
        print(x)
        exit()
    else:
        x += 1

print(-1)
