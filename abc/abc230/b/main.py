from sys import stdin
input = stdin.readline

S = input().rstrip()

T = 'oxx' * 11

if S in T:
    print("Yes")
else:
    print("No")
