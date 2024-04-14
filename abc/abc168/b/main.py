from sys import stdin
input = stdin.readline

K = int(input())
S = input().rstrip()

if len(S) <= K:
    print(S)
else:
    print(S[0:K] + '...')

