from sys import stdin
input = stdin.readline

N = int(input())
A = [*map(int, input().split())]
A_set = set()
for i in A:
    A_set.add(i)

if len(A_set) == 1:
    print("Yes")
else:
    print("No")
