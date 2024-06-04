n = int(input())
A = [*map(int, input().split())]

A.sort()
r = n
cnt = 0
res = 0
for i in range(n):
    r = max(r, i + 1)
    while r - 1 > i and A[r - 1] + A[i] >= 10**8:
        r -= 1

    cnt += n - r

for i in range(n):
    res += A[i] * (n - 1)
res -= cnt * 10**8
print(res)
