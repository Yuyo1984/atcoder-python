N, K, M = map(int, input().split())
A = [*map(int, input().split())]

x = sum(A)

y = M * N - x
if 0 <= y <= K:
    print(y)
elif y < 0:
    print(0)
else:
    print(-1)

