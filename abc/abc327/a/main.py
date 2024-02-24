from sys import stdin
input = stdin.readline

N = int(input())
S = input().rstrip()
for i in range(len(S)-1):
    if S[i] == 'a' and S[i+1] == 'b':
        print("Yes")
        exit()
    if S[i] == 'b' and S[i+1] == 'a':
        print("Yes")
        exit()

print("No")

