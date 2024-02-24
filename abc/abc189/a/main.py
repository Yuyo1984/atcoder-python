from sys import stdin
input = stdin.readline

C = set(list(input().rstrip()))

if len(C) == 1:
    print('Won')
else:
    print('Lost')
