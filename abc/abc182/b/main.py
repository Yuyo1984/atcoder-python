from sys import stdin
input = stdin.readline

N = int(input())
A = [*map(int, input().split())]
ans = 0
checker = 0
r = max(A)
for i in range(2, r+1):
    x = [a for a in A if a % i == 0]
    if len(x) >= checker and i >= ans:
        ans = i
        checker = len(x)

print(ans)
