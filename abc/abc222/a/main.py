from sys import stdin
input = stdin.readline

n = input().rstrip()

print('0' * (4 - len(n)) + n)
