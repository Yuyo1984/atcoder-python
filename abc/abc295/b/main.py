def expl(i, j, x, R, C, B):
    for h in range(-x, x + 1):
        for w in range(-x, x + 1):
            n_h = i + h
            n_w = j + w
            if (
                0 <= n_h < R
                and 0 <= n_w < C
                and (abs(h) + abs(w)) <= x
                and not ("1" <= B[n_h][n_w] <= "9")
            ):
                B[n_h][n_w] = "."
    B[i][j] = "."
    return B


R, C = map(int, input().split())
B = [list(input()) for i in range(R)]

for i in range(R):
    for j in range(C):
        if "1" <= B[i][j] <= "9":
            x = int(B[i][j])
            B = expl(i, j, x, R, C, B)

for i in range(R):
    print("".join(B[i]))
