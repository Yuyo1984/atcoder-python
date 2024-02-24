from sys import stdin
input = stdin.readline

N = int(input())
names = []
for i in range(N):
    names.append(input().rstrip())

for i in range(N, 0, -1):
    print(names[i-1])

