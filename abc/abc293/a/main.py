from sys import stdin
input = stdin.readline

S = list(input().rstrip())
for i in range(0, len(S)-1, 2):
    swap = S[i]
    S[i] = S[i+1]
    S[i+1] = swap

print("".join(S))
