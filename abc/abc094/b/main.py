N, M, X = map(int, input().split())
A = [*map(int, input().split())]

now_sq = X

pay_1, pay_2 = 0, 0
for i in range(X, -1, -1):
    if i in A:
        pay_1 += 1

for i in range(X, N + 1):
    if i in A:
        pay_2 += 1

ans = min(pay_1, pay_2)
print(ans)
