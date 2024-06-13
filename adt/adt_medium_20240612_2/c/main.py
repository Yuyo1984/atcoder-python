def rotate(grid):
    grid = grid[::-1]
    grid = list(map(list, zip(*grid)))
    return grid


# input
N = int(input())
A = []
for i in range(N):
    A.append(list(input().split()))
B = []
for i in range(N):
    B.append(list(input().split()))

# solve
X = A
for i in range(4):
    X = rotate(X)
    flag = True
    for j in range(N):
        for k in range(N):
            if X[j][k] == "1":
                if B[j][k] != "1":
                    flag = False
    if flag:
        print("Yes")
        exit()

# output
print("No")
