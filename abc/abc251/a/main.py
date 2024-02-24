from sys import stdin
input = stdin.readline

s = input().rstrip()

while len(s) < 6:
    s += s

print(s[0:6])

