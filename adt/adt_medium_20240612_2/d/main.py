# input
h, w = map(int, input().split())
A = [list(map(int, input().split())) for i in range(h)]

# solve
flag = True

for i_1 in range(h):
    for i_2 in range(i_1 + 1, h):
        for j_1 in range(w):
            for j_2 in range(j_1 + 1, w):
                x = A[i_1][j_1] + A[i_2][j_2]
                y = A[i_2][j_1] + A[i_1][j_2]
                if x > y:
                    flag = False
                    break
# output
print("Yes" if flag else "No")
