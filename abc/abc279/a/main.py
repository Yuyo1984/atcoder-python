from sys import stdin
input = stdin.readline

S = input()
print(S.count('v') + 2 * S.count('w'))

