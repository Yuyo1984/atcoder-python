from sys import stdin
input = stdin.readline

S = input().rstrip()
for i in S:
    if ord('A') <= ord(i) <= ord('Z'):
        print(S.index(i)+1)
        exit()

