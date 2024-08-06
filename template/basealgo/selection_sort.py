def minimum(A, i, N):
    minv = float("inf")

    for j in range(i, N):
        if A[j] < minv:
            minv = A[j]

    return A.index(minv)


def SelectionSort(A, N):
    for i in range(N - 1):
        minj = minimum(A, i, N)
        A[i], A[minj] = A[minj], A[i]
    return A


def main():
    A = [*map(int, input().split())]
    A = SelectionSort(A, len(A))
    print(*A)


if __name__ == "__main__":
    main()
