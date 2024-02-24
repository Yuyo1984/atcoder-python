from sys import stdin
input = stdin.readline

S = input()
if S[2] == S[3] and S[4] == S[5]:
    print('Yes')
else:
    print('No')
