from sys import stdin
input = stdin.readline

N = int(input())
S = input()
flag = False
for i in range(N):
    if S[i] == 'x':
        print("No")
        exit()
    if S[i] == 'o':
        flag = True

if flag:
    print("Yes")
else:
    print("No")
