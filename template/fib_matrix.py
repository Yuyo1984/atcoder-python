class Matrix:
    def __init__(self):
        self.p = [[0, 0], [0, 0]]


def multiplication(A, B):
    C = Matrix()
    for i in range(2):
        for k in range(2):
            for j in range(2):
                C.p[i][j] += A.p[i][k] * B.p[k][j]
                C.p[i][j] %= 1000000000
    return C


def power(A, n):
    P = A
    Q = Matrix()
    flag = False
    for i in range(60):
        if (n & (1 << i)) != 0:
            if not flag:
                Q = P
                flag = True
            else:
                Q = multiplication(Q, P)
        P = multiplication(P, P)
    return Q


def main():
    N = int(input())
    A = Matrix()
    A.p[0][0] = 1
    A.p[0][1] = 1
    A.p[1][0] = 1
    B = power(A, N - 1)
    print((B.p[1][0] + B.p[1][1]) % 1000000000)


if __name__ == "__main__":
    main()
