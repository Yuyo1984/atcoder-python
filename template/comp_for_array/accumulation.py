def accumulation(A):
    accum = [0 for i in range(len(A) + 1)]
    for i in range(len(A)):
        accum[i] = accum[i - 1] + A[i]
    return accum


def main():
    A = [*map(int, input().split())]
    AC = accumulation(A)

    Q = int(input())
    for i in range(Q):
        l, r = map(lambda x: int(x) - 1, input().split())
        res = AC[r] - AC[l - 1]
        print(res)


if __name__ == "__main__":
    main()
