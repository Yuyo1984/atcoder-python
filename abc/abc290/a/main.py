from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
A = [*map(int, input().split())]
B = [*map(int, input().split())]
ans = 0
for i in B:
    ans += A[i-1]

print(ans)
