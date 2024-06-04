# input
N, M = map(int, input().split())
A = [*map(int, input().split())]
counter = [0] * (M + 1)

# solve
for i in range(N):
    X = [*map(int, input().split())]
    for j in range(M):
        counter[j] += X[j]

flag = True
for i in range(M):
    if counter[i] < A[i]:
        flag = False

# output
if flag:
    print("Yes")
else:
    print("No")
