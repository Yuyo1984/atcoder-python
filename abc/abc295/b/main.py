def expl(i, j, x, B):
    n_h = i
    n_w = j


R, C = map(int, input().split())
B = [list(input()) for i in range(R)]

for i in range(R):
    for j in range(C):
        if "1" <= B[i][j] <= "9":
            x = int(B[i][j])
            B = expl(i, j, x, B)
