from sys import stdin
input = stdin.readline

n, a, x, y = map(int, input().split())

if n > a:
    print(x * a + y * (n - a))
else:
    print(x * n)
