from sys import stdin
input = stdin.readline

n = int(input())

print('{:02d}'.format(n % 100))
