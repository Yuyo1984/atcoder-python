from sys import stdin
input = stdin.readline

S = input().rstrip()

if S[-1] == 's':
    print(S + 'es')
else:
    print(S + 's')
