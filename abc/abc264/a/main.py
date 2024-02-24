from sys import stdin
input = stdin.readline

S = "atcoder"
L, R = map(int, input().split())
print(S[L-1:R])
