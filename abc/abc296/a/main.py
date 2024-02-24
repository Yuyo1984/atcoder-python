from sys import stdin
input = stdin.readline

N = int(input())
S = input()

flag = True
for i in range(1, len(S)):
    if S[i-1] == S[i]:
        flag = False

if flag:
    print("Yes")
else:
    print("No")
