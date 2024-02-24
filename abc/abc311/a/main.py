from sys import stdin
input = stdin.readline

N = int(input())
S = input().rstrip()
f1 = False
f2 = False
f3 = False
for i in S:
    if i == 'A':
        f1 = True
    if i == 'B':
        f2 = True
    if i == 'C':
        f3 = True
    if f1 and f2 and f3:
        print(S.index(i)+1)
        exit()

