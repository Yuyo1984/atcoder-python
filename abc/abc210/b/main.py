from sys import stdin
input = stdin.readline

N = int(input())
S = list(input().rstrip())

for i in range(len(S)):
    if S[i] == '1':
        if i % 2 == 1:
            print("Aoki")
        else:
            print("Takahashi")
        exit()
