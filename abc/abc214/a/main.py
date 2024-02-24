from sys import stdin
input = stdin.readline

n = int(input())

if n <= 125:
    print(4)
elif 126 <= n <= 211:
    print(6)
else:
    print(8)
