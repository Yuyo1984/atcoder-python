N = int(input())
A = []
for i in range(N):
    A.append(list(input()))

B = [['0' for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == 0 and 0 <= j <= N-2:
            B[i][j+1] = A[i][j]
        elif 0 <= i <= N-2 and j == N-1:
            B[i+1][j] = A[i][j]
        elif i == N-1 and 1 <= j <= N-1:
            B[i][j-1] = A[i][j]
        elif 1 <= i <= N-1 and j == 0:
            B[i-1][j] = A[i][j]
        else:
            B[i][j] = A[i][j]

for i in range(N):
    print(''.join(B[i]))
