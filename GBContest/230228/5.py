import sys
input = sys.stdin.readline
import math
import numpy

odd = input().rstrip()
even = input().rstrip()

ans = ""
x = len(odd) + len(even)
for i in range(x):
    if i % 2 == 0:
        ans += even[i]
    else:
        ans += odd[i]

print(ans)

