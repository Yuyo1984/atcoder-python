from sys import stdin
input = stdin.readline

N = int(input())
A = [*map(int, input().split())]
B = [*map(int, input().split())]

a = max(A)
b = min(B)

if a > b:
    print(0)
else:
    print(b - a + 1)

