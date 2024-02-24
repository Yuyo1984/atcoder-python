from sys import stdin
input = stdin.readline

S = list(input().rstrip())
for i in range(len(S)-1, -1, -1):
    if S[i] == 'a':
        print(i+1)
        exit()

print(-1)

