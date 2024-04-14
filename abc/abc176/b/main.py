from sys import stdin
input = stdin.readline

N = input().rstrip()
x = 0
for i in range(len(N)):
    x += int(N[i])

if x % 9 == 0:
    print("Yes")
else:
    print("No")
