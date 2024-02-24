from sys import stdin
input = stdin.readline

L, R = map(int, input().split())
S = input()

print(S[:L-1] + ''.join(list(reversed(S[L-1:R]))) + S[R:])
