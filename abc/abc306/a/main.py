from sys import stdin
input = stdin.readline

N = int(input())
S = input().rstrip()
for i in S:
    print(i*2,end="")

