from sys import stdin
input = stdin.readline

k = int(input())

H = 21
if k >= 60:
    H += 1

M = '{:02d}'.format(k % 60)

print(str(H) + ':' + str(M))
