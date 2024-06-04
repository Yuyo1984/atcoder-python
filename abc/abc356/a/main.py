N, L, R = map(int, input().split())
L -= 1
R -= 1
A = [i for i in range(1, N + 1)]
x = A[L : R + 1]
x = x[::-1]
ans = A[:L] + x + A[R + 1 :]
print(*ans)
