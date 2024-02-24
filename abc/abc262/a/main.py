from sys import stdin
input = stdin.readline

y = int(input())

if y % 4 == 2:
    print(y)
elif y % 4 == 0:
    print(y + 2)
elif y % 4 == 3:
    print(y + 3)
else:
    print(y + 1)
