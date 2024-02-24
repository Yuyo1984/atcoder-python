from sys import stdin
input = stdin.readline

N = int(input())
S = list(input().rstrip().split('.'))
S = "".join(S)
if S == "|*|":
    print("in")
else:
    print("out")

