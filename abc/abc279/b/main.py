from sys import stdin
input = stdin.readline

S = input().rstrip()
T = input().rstrip()

if T in S:
    print('Yes')
else:
    print('No')


