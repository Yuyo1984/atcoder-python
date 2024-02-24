from sys import stdin
input = stdin.readline

a, b = map(int, input().split())

if a > 0 and b == 0:
    print('Gold')
elif a == 0 and b > 0:
    print('Silver')
else:
    print('Alloy')
