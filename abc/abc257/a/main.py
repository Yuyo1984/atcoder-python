from sys import stdin
input = stdin.readline

n, x = map(int, input().split())

print(chr(64 + ((x + n - 1) // n)))
