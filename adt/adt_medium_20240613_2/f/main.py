# input
N = int(input())
S = [*map(int, input().split())]
T = [*map(int, input().split())]
# solve
for i in range(2 * N):
    T[(i + 1) % N] = min(T[(i + 1) % N], T[i % N] + S[i % N])
# output
for ans in T:
    print(ans)
