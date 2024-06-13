# input
N, K = map(int, input().split())
# solve
sum_P = []
pk = []
for i in range(N):
    a, b, c = map(int, input().split())
    x = a + b + c
    sum_P.append(x)
    pk.append(x)

pk.sort(reverse=True)

for i in range(N):
    x = sum_P[i] + 300
    flag = False
    if x >= pk[K - 1]:
        flag = True
    print("Yes" if flag else "No")
# output
