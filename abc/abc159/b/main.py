from sys import stdin
input = stdin.readline

S = input().rstrip()
T = S[0:len(S)//2]
U = S[len(S)//2+1:]
if S == S[::-1] and T == T[::-1] and U == U[::-1]:
    print("Yes")
else:
    print("No")

