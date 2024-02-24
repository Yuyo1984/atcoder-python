from sys import stdin
input = stdin.readline
import math

a, b = map(int, input().rstrip().split())

c = math.sqrt(a**2 + b**2)

print('{:.10f}'.format(a/c), '{:.10f}'.format(b/c))
