from sys import stdin
input = stdin.readline

N = int(input())
S = input().rstrip()
T = input().rstrip()
S = S.replace('1', 'l').replace('0', 'o')
T = T.replace('1', 'l').replace('0', 'o')
if S == T:
    print("Yes")
else:
    print("No")
