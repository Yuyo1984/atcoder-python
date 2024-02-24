from sys import stdin
input = stdin.readline

S = input().rstrip()
S = S.replace('6', 'x').replace('9', '6').replace('x', '9')

print(S[::-1])