from sys import stdin
input = stdin.readline

S = input().rstrip()
T = input().rstrip()

for i in range(len(S)):
    if S[i] != T[i]:
        print(i + 1)
        exit()

print(len(T))

