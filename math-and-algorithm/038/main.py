N, Q = map(int, input().split())
A = [0] + [*map(int, input().split())]
S = [0 for i in range(N + 1)]
for i in range(1, N + 1):
    S[i] = S[i - 1] + A[i]

for i in range(Q):
    L, R = map(int, input().split())
    print(S[R] - S[L - 1])
