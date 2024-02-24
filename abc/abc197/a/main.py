from sys import stdin
input = stdin.readline

s = input().rstrip()

print(s[1:] + s[0])
