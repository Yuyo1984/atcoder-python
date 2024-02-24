from sys import stdin
input = stdin.readline

n = input().rstrip()

x = int(n[0] + n[1] + n[2])
y = int(n[1] + n[2] + n[0])
z = int(n[2] + n[0] + n[1])

print(x+y+z)
