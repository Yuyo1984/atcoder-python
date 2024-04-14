from sys import stdin
input = stdin.readline
import math

N = int(input())
x = [*map(int, input().split())]

ans1 = sum([abs(i) for i in x])
ans2 = math.sqrt(sum([i ** 2 for i in x]))
ans3 = max([abs(i) for i in x])

print(ans1)
print(ans2)
print(ans3)
