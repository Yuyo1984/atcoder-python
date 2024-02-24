from sys import stdin
input = stdin.readline

s = input().rstrip()
a, b = map(int, input().split())

print(s[0:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:])
