# func

# input
N = int(input())
grid_A = []
for i in range(N):
    grid_A.append(list(input()))
grid_B = []
for i in range(N):
    grid_B.append(list(input()))

# solve
for i in range(N):
    for j in range(N):
        if grid_A[i][j] != grid_B[i][j]:
            print(i+1, j+1)
            exit()

# answer
