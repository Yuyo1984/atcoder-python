from sys import stdin
input = stdin.readline

a, b, c, x = map(int, input().split())

if x <= a:
    print('{:.12f}'.format(1))
else:
    ans = c / (b - a)
    if b < x:
        ans = 0
    print('{:.12f}'.format(ans))

