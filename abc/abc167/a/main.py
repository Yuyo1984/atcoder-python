from sys import stdin
input = stdin.readline

S = input().rstrip()
T = input().rstrip()

if T[0:-1] == S:
    print('Yes')
else:
    print('No')
