from sys import stdin
input = stdin.readline

x = [*map(int, input().split())]

x.sort()

if x[0] == x[1]:
    print(x[2])
elif x[1] == x[2]:
    print(x[0])
elif x[0] == x[2]:
    print(x[1])
else:
    print(0)
