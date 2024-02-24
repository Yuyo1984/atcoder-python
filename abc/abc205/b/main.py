from sys import stdin
input = stdin.readline

N = int(input())
A = set([*map(int, input().split())])

perm = set([(i+1) for i in range(N)])
if A == perm:
    print("Yes")
else:
    print("No")
