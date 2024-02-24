from sys import stdin
input = stdin.readline

S = input().rstrip()

print(S[0:len(S)-1] + '4')
