import sys

N, L, W = map(int, input().split())
A = [*map(int, input().split())]
flag = [False] * L
ans = 0
for i in range(len(A)):
    x = A[i] - 1
    for j in range(x, x+W+1):
        if j == len(A)-1:
            break
        flag[j] = True

for i in range(0, N+1, W):
    if not all(flag[i:i+W]):
        ans += 1

print(ans)
