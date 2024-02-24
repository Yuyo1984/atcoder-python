from sys import stdin
input = stdin.readline
import math

n = int(input())

x = math.floor(1.08 * n)

if x < 206:
    print('Yay!')
elif x == 206:
    print('so-so')
else:
    print(':(')
