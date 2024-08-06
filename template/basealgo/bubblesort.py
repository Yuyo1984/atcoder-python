def BubbleSort(A, N):
    for i in range(N - 1):
        for j in range(N - 1, i, -1):
            if A[j - 1] > A[j]:
                A[j - 1], A[j] = A[j], A[j - 1]


def main():
    A = [*map(int, input().split())]
    BubbleSort(A, len(A))
    print(*A)


if __name__ == "__main__":
    main()
