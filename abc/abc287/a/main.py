from sys import stdin
input = stdin.readline

N = int(input())
p = 0
n = 0
for i in range(N):
    x = input().rstrip()
    if x == "For":
        p += 1
    else:
        n += 1

if p > n:
    print("Yes")
else:
    print("No")
